from typing import Any, Awaitable, Callable

from aiogram.types import TelegramObject

from app.presentation.telegram.enums import MiddlewareEventType
from app.presentation.telegram.middlewares.event_typed import EventTypedMiddleware


class UpdateLoggingMiddleware(EventTypedMiddleware):
    """Structured log line per processed update: update_id, user_id, type, duration, outcome."""

    __event_types__ = [MiddlewareEventType.UPDATE]

    async def __call__(
        self,
        handler: Callable[[TelegramObject, dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: dict[str, Any],
    ) -> Any:
        # TODO(M5): never log message text or tokens
        return await handler(event, data)
