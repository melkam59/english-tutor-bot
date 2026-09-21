from datetime import datetime
from typing import Optional, Protocol

from app.domain.user import User


class UsersGateway(Protocol):
    async def get(self, user_id: int) -> Optional[User]: ...

    async def create(
        self,
        user_id: int,
        name: str,
        username: Optional[str],
        language: str,
        language_code: Optional[str],
    ) -> User: ...

    async def save(self, user: User) -> None: ...

    async def count(self) -> int: ...

    async def count_active_since(self, since: datetime) -> int: ...

    async def count_created_since(self, since: datetime) -> int: ...

    async def get_broadcast_ids(self, limit: int, offset: int) -> list[int]: ...
