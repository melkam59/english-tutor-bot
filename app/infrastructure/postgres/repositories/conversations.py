from dataclasses import dataclass
from typing import Optional

from sqlalchemy import select

from app.application.ports.repositories.conversations import ConversationsGateway
from app.domain.conversation import Conversation
from app.domain.enums.practice_mode import PracticeMode, RolePlayScenario
from app.infrastructure.postgres.repository_helper import SqlRepositoryHelper
from app.infrastructure.postgres.uow import UoW


@dataclass
class ConversationsRepository(ConversationsGateway):
    _uow: UoW
    _helper: SqlRepositoryHelper[Conversation]

    async def get_active(self, user_id: int) -> Optional[Conversation]:
        query = (
            select(Conversation)
            .where(Conversation.user_id == user_id, Conversation.is_active.is_(True))
            .order_by(Conversation.id.desc())
            .limit(1)
        )
        return await self._helper.session.scalar(query)

    async def create(
        self,
        user_id: int,
        mode: PracticeMode,
        scenario: Optional[RolePlayScenario] = None,
    ) -> Conversation:
        conversation = Conversation(user_id=user_id, mode=mode, scenario=scenario)
        await self._uow.commit(conversation)
        return conversation

    async def save(self, conversation: Conversation) -> None:
        await self._uow.commit(conversation)

    async def deactivate_all(self, user_id: int) -> None:
        await self._helper.update(Conversation.user_id == user_id, is_active=False)
        await self._uow.commit()

    async def count(self, user_id: int) -> int:
        return await self._helper.count(Conversation.user_id == user_id)
