from dataclasses import dataclass

from sqlalchemy import func, select

from app.application.models.dto.llm import Correction
from app.application.ports.repositories.mistakes import MistakesGateway
from app.domain.enums.mistake_category import MistakeCategory
from app.domain.user_mistake import UserMistake
from app.infrastructure.postgres.repository_helper import SqlRepositoryHelper
from app.infrastructure.postgres.uow import UoW


@dataclass
class MistakesRepository(MistakesGateway):
    _uow: UoW
    _helper: SqlRepositoryHelper[UserMistake]

    async def add_many(self, user_id: int, corrections: list[Correction]) -> None:
        await self._uow.commit(
            *(
                UserMistake(user_id=user_id, **correction.model_dump())
                for correction in corrections
            )
        )

    async def get_recent(self, user_id: int, limit: int) -> list[UserMistake]:
        query = (
            select(UserMistake)
            .where(UserMistake.user_id == user_id)
            .order_by(UserMistake.id.desc())
            .limit(limit)
        )
        return list(reversed((await self._helper.session.scalars(query)).all()))

    async def get_top_categories(
        self,
        user_id: int,
        limit: int,
    ) -> list[tuple[MistakeCategory, int]]:
        total = func.count().label("total")
        query = (
            select(UserMistake.category, total)
            .where(UserMistake.user_id == user_id)
            .group_by(UserMistake.category)
            .order_by(total.desc())
            .limit(limit)
        )
        rows = await self._helper.session.execute(query)
        return [(category, count) for category, count in rows.all()]
