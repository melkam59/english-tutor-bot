from dataclasses import dataclass

from app.application.ports.limits.rate_limiter import Throttler, UsageCounter
from app.infrastructure.redis.repository import RedisRepository


@dataclass
class RedisUsageCounter(UsageCounter):
    """Keys: ``DailyMessagesKey`` / ``DailyVoiceMessagesKey``, expire after 24-48h."""

    repository: RedisRepository

    async def get_messages(self, user_id: int) -> int:
        # TODO(M2)
        raise NotImplementedError

    async def increment_messages(self, user_id: int) -> int:
        # TODO(M2): INCR + EXPIRE
        raise NotImplementedError

    async def get_voice_messages(self, user_id: int) -> int:
        # TODO(M4)
        raise NotImplementedError

    async def increment_voice_messages(self, user_id: int) -> int:
        # TODO(M4)
        raise NotImplementedError


@dataclass
class RedisThrottler(Throttler):
    """Keys: ``ThrottleKey`` / ``UpdateDedupKey``, both are plain ``SET NX EX``."""

    repository: RedisRepository

    async def is_throttled(self, user_id: int, rate: float) -> bool:
        # TODO(M2)
        raise NotImplementedError

    async def is_duplicate_update(self, bot_id: int, update_id: int, ttl: int) -> bool:
        # TODO(M5)
        raise NotImplementedError
