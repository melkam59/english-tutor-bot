from dataclasses import dataclass
from typing import Any

from app.application.interactors.limits.usage import UsageLimitsInteractor
from app.application.interactors.subscription.manage import SubscriptionInteractor
from app.domain.user import User
from app.presentation.telegram.flows.base import BaseFlow
from app.presentation.telegram.presenters.common.subscription import SubscriptionPresenter
from app.presentation.telegram.view.renderer import Renderer


@dataclass(frozen=True)
class SubscriptionFlow(BaseFlow):
    user: User
    interactor: SubscriptionInteractor
    limits: UsageLimitsInteractor
    presenter: SubscriptionPresenter
    renderer: Renderer

    async def show_plans(self) -> Any:
        return await self.renderer.apply(self.presenter.plans(user=self.user))

    async def buy_premium(self, months: int) -> Any:
        # TODO(M4): no real payments in the MVP; plug PaymentsGateway (Telegram Stars) in here
        return await self.renderer.apply(self.presenter.not_implemented())
