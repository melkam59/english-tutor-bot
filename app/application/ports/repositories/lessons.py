from typing import Optional, Protocol

from app.domain.enums.english_level import EnglishLevel
from app.domain.lesson import Lesson
from app.utils.custom_types import DictStrAny


class LessonsGateway(Protocol):
    async def get(self, lesson_id: int, user_id: int) -> Optional[Lesson]: ...

    async def create(
        self,
        user_id: int,
        topic: str,
        level: EnglishLevel,
        content: DictStrAny,
    ) -> Lesson: ...

    async def save(self, lesson: Lesson) -> None: ...

    async def count_completed(self, user_id: int) -> int: ...
