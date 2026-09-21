from dataclasses import dataclass

from app.application.models.dto.limits import DailyUsage
from app.domain.user import User
from app.presentation.telegram.keyboards.menu import subscription_keyboard
from app.presentation.telegram.presenters.base import BasePresenter
from app.presentation.telegram.view.models import View


@dataclass(frozen=True)
class SubscriptionPresenter(BasePresenter):
    def plans(self, user: User) -> View:
        return View(
            text=self.i18n.messages.subscription.plans(plan=user.subscription_type),
            reply_markup=subscription_keyboard(i18n=self.i18n),
            edit=False,
        )

    def status(self, user: User, usage: DailyUsage) -> View:
        # TODO(M4): current plan, expiration date and today's usage
        raise NotImplementedError
