from typing import Any, Awaitable, Callable

from aiogram.types import TelegramObject

from app.presentation.telegram.enums import MiddlewareEventType
from app.presentation.telegram.middlewares.event_typed import EventTypedMiddleware


class UpdateDedupMiddleware(EventTypedMiddleware):
    """Drops updates Telegram delivered twice (webhook retries)."""

    __event_types__ = [MiddlewareEventType.UPDATE]

    async def __call__(
        self,
        handler: Callable[[TelegramObject, dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: dict[str, Any],
    ) -> Any:
        # TODO(M5): Throttler.is_duplicate_update(bot_id, update_id, ttl=limits.update_dedup_ttl)
        return await handler(event, data)


class ThrottlingMiddleware(EventTypedMiddleware):
    """Per-user rate limiting and protection from repeated requests."""

    __event_types__ = [MiddlewareEventType.MESSAGE, MiddlewareEventType.CALLBACK_QUERY]

    async def __call__(
        self,
        handler: Callable[[TelegramObject, dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: dict[str, Any],
    ) -> Any:
        # TODO(M2): Throttler.is_throttled(user_id, rate=limits.throttle_rate) -> skip silently
        return await handler(event, data)
