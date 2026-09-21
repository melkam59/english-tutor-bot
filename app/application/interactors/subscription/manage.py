from dataclasses import dataclass

from app.application.interactors.base import BaseInteractor
from app.application.ports.repositories.users import UsersGateway
from app.domain.user import User


@dataclass(frozen=True)
class SubscriptionInteractor(BaseInteractor):
    """
    Subscription status only. Real payments (Telegram Stars, ...) plug in through
    ``app.application.ports.payments.gateway.PaymentsGateway`` later.
    """

    user: User
    users_gateway: UsersGateway

    async def activate_premium(self, days: int) -> None:
        # TODO(M4): extend from max(now, subscription_expires_at)
        raise NotImplementedError

    async def cancel_premium(self) -> None:
        # TODO(M4)
        raise NotImplementedError
