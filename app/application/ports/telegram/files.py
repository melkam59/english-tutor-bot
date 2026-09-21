from typing import Protocol


class TelegramFiles(Protocol):
    async def download(self, file_id: str) -> bytes: ...
