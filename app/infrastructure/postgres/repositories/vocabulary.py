from dataclasses import dataclass

from app.application.ports.repositories.vocabulary import VocabularyGateway
from app.domain.vocabulary_item import VocabularyItem
from app.infrastructure.postgres.repository_helper import SqlRepositoryHelper
from app.infrastructure.postgres.uow import UoW


@dataclass
class VocabularyRepository(VocabularyGateway):
    # TODO(M3): implement the remaining methods of VocabularyGateway
    _uow: UoW
    _helper: SqlRepositoryHelper[VocabularyItem]

    async def count(self, user_id: int) -> int:
        return await self._helper.count(VocabularyItem.user_id == user_id)
