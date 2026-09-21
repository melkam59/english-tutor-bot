from dataclasses import dataclass

from app.application.interactors.base import BaseInteractor
from app.application.models.dto.admin import AdminStats
from app.application.ports.repositories.usage import UsageGateway
from app.application.ports.repositories.users import UsersGateway


@dataclass(frozen=True)
class AdminStatsInteractor(BaseInteractor):
    users_gateway: UsersGateway
    usage_gateway: UsageGateway

    async def get_stats(self, days: int = 1) -> AdminStats:
        # TODO(M4)
        raise NotImplementedError
