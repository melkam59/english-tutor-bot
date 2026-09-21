from dataclasses import dataclass

from aiogram import Bot

from app.application.ports.telegram.files import TelegramFiles


@dataclass
class TelegramFilesImpl(TelegramFiles):
    bot: Bot

    async def download(self, file_id: str) -> bytes:
        # TODO(M4): bot.download(file_id) into BytesIO
        raise NotImplementedError
