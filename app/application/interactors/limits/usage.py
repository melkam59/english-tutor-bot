from dataclasses import dataclass

from app.application.interactors.base import BaseInteractor
from app.application.models.config import AppConfig
from app.application.models.dto.limits import DailyUsage
from app.application.models.dto.llm import LLMUsage
from app.application.ports.limits.rate_limiter import UsageCounter
from app.application.ports.repositories.usage import UsageGateway
from app.application.services.access import AccessPolicy
from app.application.services.cost import CostEstimator
from app.domain.enums.request_type import RequestType
from app.domain.user import User


@dataclass(frozen=True)
class UsageLimitsInteractor(BaseInteractor):
    """Daily quotas, input validation and token/cost logging."""

    user: User
    config: AppConfig
    access: AccessPolicy
    counter: UsageCounter
    cost: CostEstimator
    usage_gateway: UsageGateway

    async def check_text_message(self, text: str) -> None:
        # TODO(M2): InputTooLongError / DailyLimitReachedError
        raise NotImplementedError

    async def check_voice_message(self, duration: int) -> None:
        # TODO(M4): VoiceTooLongError / VoiceLimitReachedError / DailyLimitReachedError
        raise NotImplementedError

    async def get_daily_usage(self) -> DailyUsage:
        # TODO(M2)
        raise NotImplementedError

    async def record_llm_usage(self, request_type: RequestType, usage: LLMUsage) -> None:
        # TODO(M4): increment the daily counter, insert UsageRecord with estimated cost
        raise NotImplementedError

    async def record_stt_usage(self, duration: int) -> None:
        # TODO(M4)
        raise NotImplementedError
