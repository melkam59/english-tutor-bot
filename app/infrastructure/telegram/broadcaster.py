from dataclasses import dataclass

from aiogram import Bot

from app.application.ports.telegram.broadcaster import Broadcaster


@dataclass
class BroadcasterImpl(Broadcaster):
    bot: Bot

    async def send(self, chat_id: int, text: str) -> bool:
        # TODO(M4): handle TelegramRetryAfter (sleep + retry) and TelegramForbiddenError (False)
        raise NotImplementedError
