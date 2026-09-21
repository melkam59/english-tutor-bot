from dataclasses import dataclass
from typing import Final

from app.application.ports.limits.rate_limiter import Throttler, UsageCounter
from app.application.storage.keys.base import StorageKey
from app.application.storage.keys.impl import DailyMessagesKey, DailyVoiceMessagesKey
from app.infrastructure.redis.repository import RedisRepository
from app.utils.time import datetime_now

_COUNTER_TTL: Final[int] = 60 * 60 * 48


def _today() -> str:
    return datetime_now().date().isoformat()


@dataclass
class RedisUsageCounter(UsageCounter):
    """Keys: ``DailyMessagesKey`` / ``DailyVoiceMessagesKey``, expire after 24-48h."""

    repository: RedisRepository

    async def _get(self, key: StorageKey[int]) -> int:
        return int(await self.repository.client.get(key.pack()) or 0)

    async def _increment(self, key: StorageKey[int]) -> int:
        value: int = await self.repository.client.incr(key.pack())
        await self.repository.client.expire(key.pack(), _COUNTER_TTL)
        return value

    async def get_messages(self, user_id: int) -> int:
        return await self._get(DailyMessagesKey(user_id=user_id, day=_today()))

    async def increment_messages(self, user_id: int) -> int:
        return await self._increment(DailyMessagesKey(user_id=user_id, day=_today()))

    async def get_voice_messages(self, user_id: int) -> int:
        return await self._get(DailyVoiceMessagesKey(user_id=user_id, day=_today()))

    async def increment_voice_messages(self, user_id: int) -> int:
        return await self._increment(DailyVoiceMessagesKey(user_id=user_id, day=_today()))


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
