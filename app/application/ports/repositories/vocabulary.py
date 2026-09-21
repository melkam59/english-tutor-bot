from datetime import datetime
from typing import Optional, Protocol

from app.domain.vocabulary_item import VocabularyItem


class VocabularyGateway(Protocol):
    async def get(self, item_id: int, user_id: int) -> Optional[VocabularyItem]: ...

    async def add(
        self,
        user_id: int,
        phrase: str,
        translation: str,
        example: Optional[str],
    ) -> VocabularyItem: ...

    async def save(self, item: VocabularyItem) -> None: ...

    async def delete(self, item: VocabularyItem) -> None: ...

    async def get_page(self, user_id: int, limit: int, offset: int) -> list[VocabularyItem]: ...

    async def get_due(self, user_id: int, now: datetime, limit: int) -> list[VocabularyItem]: ...

    async def get_recent(self, user_id: int, limit: int) -> list[VocabularyItem]: ...

    async def count(self, user_id: int) -> int: ...

    async def get_user_ids_with_due_items(self, now: datetime) -> list[int]: ...
