from dataclasses import dataclass

from app.application.errors.limits import DailyLimitReachedError, InputTooLongError
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
        if len(text) > self.config.limits.max_input_length:
            raise InputTooLongError()
        limit: int = self._messages_limit()
        if limit and await self.counter.get_messages(user_id=self.user.id) >= limit:
            raise DailyLimitReachedError()

    async def check_voice_message(self, duration: int) -> None:
        # TODO(M4): VoiceTooLongError / VoiceLimitReachedError / DailyLimitReachedError
        raise NotImplementedError

    def _messages_limit(self) -> int:
        limits = self.config.limits
        if self.access.is_premium(self.user):
            return limits.premium_daily_messages
        return limits.free_daily_messages

    def _voice_limit(self) -> int:
        limits = self.config.limits
        if self.access.is_premium(self.user):
            return limits.premium_daily_voice_messages
        return limits.free_daily_voice_messages

    async def get_daily_usage(self) -> DailyUsage:
        return DailyUsage(
            messages_used=await self.counter.get_messages(user_id=self.user.id),
            messages_limit=self._messages_limit(),
            voice_used=await self.counter.get_voice_messages(user_id=self.user.id),
            voice_limit=self._voice_limit(),
        )

    async def record_llm_usage(self, request_type: RequestType, usage: LLMUsage) -> None:
        await self.counter.increment_messages(user_id=self.user.id)
        await self.usage_gateway.add(
            user_id=self.user.id,
            request_type=request_type,
            input_tokens=usage.input_tokens,
            output_tokens=usage.output_tokens,
            estimated_cost=self.cost.llm_cost(usage),
        )

    async def record_stt_usage(self, duration: int) -> None:
        # TODO(M4)
        raise NotImplementedError
