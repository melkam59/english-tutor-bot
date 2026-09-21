from dataclasses import dataclass
from datetime import datetime
from typing import Optional

from app.application.ports.repositories.users import UsersGateway
from app.domain.user import User
from app.infrastructure.postgres.repository_helper import SqlRepositoryHelper
from app.infrastructure.postgres.uow import UoW


@dataclass
class UsersRepository(UsersGateway):
    _uow: UoW
    _helper: SqlRepositoryHelper[User]

    async def get(self, user_id: int) -> Optional[User]:
        return await self._helper.get_one(User.id == user_id)

    async def create(
        self,
        user_id: int,
        name: str,
        username: Optional[str],
        language: str,
        language_code: Optional[str],
    ) -> User:
        user: User = User(
            id=user_id,
            name=name,
            username=username,
            language=language,
            language_code=language_code,
        )
        await self._uow.commit(user)
        return user

    async def save(self, user: User) -> None:
        await self._uow.commit(user)

    async def count(self) -> int:
        return await self._helper.count()

    async def count_active_since(self, since: datetime) -> int:
        return await self._helper.count(User.last_activity_at >= since)

    async def count_created_since(self, since: datetime) -> int:
        return await self._helper.count(User.created_at >= since)

    async def get_broadcast_ids(self, limit: int, offset: int) -> list[int]:
        # TODO(M4): ids of users with blocked_at IS NULL AND banned_at IS NULL, ordered by id
        raise NotImplementedError
