from typing import Protocol

from app.domain.enums.message_role import MessageRole
from app.domain.message import Message


class MessagesGateway(Protocol):
    async def add(
        self,
        conversation_id: int,
        role: MessageRole,
        text: str,
        token_usage: int = 0,
    ) -> Message: ...

    async def get_recent(self, conversation_id: int, limit: int) -> list[Message]: ...

    async def count(self, conversation_id: int) -> int: ...
