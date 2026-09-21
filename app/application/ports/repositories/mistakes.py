from typing import Protocol

from app.application.models.dto.llm import Correction
from app.domain.enums.mistake_category import MistakeCategory
from app.domain.user_mistake import UserMistake


class MistakesGateway(Protocol):
    async def add_many(self, user_id: int, corrections: list[Correction]) -> None: ...

    async def get_recent(self, user_id: int, limit: int) -> list[UserMistake]: ...

    async def get_top_categories(
        self,
        user_id: int,
        limit: int,
    ) -> list[tuple[MistakeCategory, int]]: ...
