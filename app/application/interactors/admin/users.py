from dataclasses import dataclass

from app.application.interactors.base import BaseInteractor
from app.application.ports.repositories.users import UsersGateway


@dataclass(frozen=True)
class AdminUsersInteractor(BaseInteractor):
    users_gateway: UsersGateway

    async def ban(self, user_id: int) -> None:
        # TODO(M4)
        raise NotImplementedError

    async def unban(self, user_id: int) -> None:
        # TODO(M4)
        raise NotImplementedError

    async def grant_premium(self, user_id: int, days: int) -> None:
        # TODO(M4)
        raise NotImplementedError

    async def revoke_premium(self, user_id: int) -> None:
        # TODO(M4)
        raise NotImplementedError
