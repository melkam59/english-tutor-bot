from dataclasses import dataclass

from app.application.interactors.base import BaseInteractor
from app.application.models.dto.admin import BroadcastResult
from app.application.ports.repositories.users import UsersGateway
from app.application.ports.telegram.broadcaster import Broadcaster


@dataclass(frozen=True)
class BroadcastInteractor(BaseInteractor):
    users_gateway: UsersGateway
    broadcaster: Broadcaster

    async def broadcast(self, text: str) -> BroadcastResult:
        # TODO(M4): paginate users_gateway.get_broadcast_ids, respect Telegram flood limits
        #  (~25 msg/s), consider moving into the background worker for big audiences
        raise NotImplementedError
