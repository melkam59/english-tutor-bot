from typing import Protocol


class Broadcaster(Protocol):
    async def send(self, chat_id: int, text: str) -> bool:
        """:return: False when the message could not be delivered"""
        ...
