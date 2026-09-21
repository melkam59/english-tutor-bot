from dataclasses import dataclass

from app.domain.user import User
from app.presentation.telegram.presenters.base import BasePresenter
from app.presentation.telegram.view.models import View


@dataclass(frozen=True)
class CommonMenuPresenter(BasePresenter):
    def greeting(self, user: User) -> View:
        return View(text=self.i18n.messages.greeting(name=user.mention))

    def help(self) -> View:
        return View(text=self.i18n.messages.help(), edit=False)
