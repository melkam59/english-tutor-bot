from typing import Any, Awaitable, Callable

from aiogram.types import TelegramObject

from app.presentation.telegram.enums import MiddlewareEventType
from app.presentation.telegram.middlewares.event_typed import EventTypedMiddleware


class BanMiddleware(EventTypedMiddleware):
    """Ignores every update from users banned by an admin."""

    __event_types__ = [MiddlewareEventType.MESSAGE, MiddlewareEventType.CALLBACK_QUERY]

    async def __call__(
        self,
        handler: Callable[[TelegramObject, dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: dict[str, Any],
    ) -> Any:
        # TODO(M4): resolve User from the dishka request container, drop if user.is_banned
        return await handler(event, data)
