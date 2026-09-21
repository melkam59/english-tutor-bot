from datetime import timedelta
from decimal import Decimal

import pytest

from app.application.errors.limits import DailyLimitReachedError, InputTooLongError
from app.application.interactors.limits.usage import UsageLimitsInteractor
from app.application.models.dto.llm import LLMUsage
from app.application.services.access import AccessPolicy
from app.application.services.cost import CostEstimator
from app.domain.enums.request_type import RequestType
from app.domain.enums.subscription import SubscriptionType
from app.domain.user import User
from app.providers.infrastructure.app import create_app_config
from app.utils.time import datetime_now
from tests.mocks.gateways import FakeUsageCounter, FakeUsageGateway, make_user

USAGE = LLMUsage(input_tokens=1_000_000, output_tokens=500_000)


def make_limits(user: User) -> tuple[UsageLimitsInteractor, FakeUsageGateway]:
    config = create_app_config()
    config.limits.free_daily_messages = 2
    config.limits.premium_daily_messages = 0
    config.limits.max_input_length = 50
    config.llm.input_price_per_million = 0.5
    config.llm.output_price_per_million = 2.0
    usage_gateway = FakeUsageGateway()
    interactor = UsageLimitsInteractor(
        user=user,
        config=config,
        access=AccessPolicy(),
        counter=FakeUsageCounter(),
        cost=CostEstimator(config=config),
        usage_gateway=usage_gateway,
    )
    return interactor, usage_gateway


async def test_free_user_is_blocked_after_daily_limit() -> None:
    limits, _ = make_limits(make_user())

    for _ in range(2):
        await limits.check_text_message("Hello")
        await limits.record_llm_usage(RequestType.CHAT, USAGE)

    with pytest.raises(DailyLimitReachedError):
        await limits.check_text_message("Hello")


async def test_premium_user_is_not_limited() -> None:
    premium = make_user(
        subscription_type=SubscriptionType.PREMIUM,
        subscription_expires_at=datetime_now() + timedelta(days=30),
    )
    limits, _ = make_limits(premium)

    for _ in range(5):
        await limits.check_text_message("Hello")
        await limits.record_llm_usage(RequestType.CHAT, USAGE)


async def test_expired_premium_is_limited_like_free() -> None:
    expired = make_user(
        subscription_type=SubscriptionType.PREMIUM,
        subscription_expires_at=datetime_now() - timedelta(days=1),
    )
    limits, _ = make_limits(expired)

    for _ in range(2):
        await limits.record_llm_usage(RequestType.CHAT, USAGE)

    with pytest.raises(DailyLimitReachedError):
        await limits.check_text_message("Hello")


async def test_too_long_input_is_rejected() -> None:
    limits, _ = make_limits(make_user())

    with pytest.raises(InputTooLongError):
        await limits.check_text_message("a" * 51)


async def test_token_usage_is_logged_with_estimated_cost() -> None:
    limits, usage_gateway = make_limits(make_user())

    await limits.record_llm_usage(RequestType.CHAT, USAGE)

    record = usage_gateway.items[0]
    assert (record.input_tokens, record.output_tokens) == (1_000_000, 500_000)
    # 1M input * $0.5 + 0.5M output * $2.0
    assert record.estimated_cost == Decimal("1.5")
