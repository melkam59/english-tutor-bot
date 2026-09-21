from dataclasses import dataclass

from app.application.ports.repositories.lessons import LessonsGateway
from app.domain.lesson import Lesson
from app.infrastructure.postgres.repository_helper import SqlRepositoryHelper
from app.infrastructure.postgres.uow import UoW


@dataclass
class LessonsRepository(LessonsGateway):
    # TODO(M3): implement the remaining methods of LessonsGateway
    _uow: UoW
    _helper: SqlRepositoryHelper[Lesson]

    async def count_completed(self, user_id: int) -> int:
        return await self._helper.count(
            Lesson.user_id == user_id, Lesson.completed_at.is_not(None)
        )
