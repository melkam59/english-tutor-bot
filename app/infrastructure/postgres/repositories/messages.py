from dataclasses import dataclass

from sqlalchemy import select

from app.application.ports.repositories.messages import MessagesGateway
from app.domain.enums.message_role import MessageRole
from app.domain.message import Message
from app.infrastructure.postgres.repository_helper import SqlRepositoryHelper
from app.infrastructure.postgres.uow import UoW


@dataclass
class MessagesRepository(MessagesGateway):
    _uow: UoW
    _helper: SqlRepositoryHelper[Message]

    async def add(
        self,
        conversation_id: int,
        role: MessageRole,
        text: str,
        token_usage: int = 0,
    ) -> Message:
        message = Message(
            conversation_id=conversation_id,
            role=role,
            text=text,
            token_usage=token_usage,
        )
        await self._uow.commit(message)
        return message

    async def get_recent(self, conversation_id: int, limit: int) -> list[Message]:
        query = (
            select(Message)
            .where(Message.conversation_id == conversation_id)
            .order_by(Message.id.desc())
            .limit(limit)
        )
        return list(reversed((await self._helper.session.scalars(query)).all()))

    async def count(self, conversation_id: int) -> int:
        return await self._helper.count(Message.conversation_id == conversation_id)
