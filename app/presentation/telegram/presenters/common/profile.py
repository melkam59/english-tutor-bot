from dataclasses import dataclass

from app.domain.user import User
from app.presentation.telegram.keyboards.settings import settings_keyboard
from app.presentation.telegram.presenters.base import BasePresenter
from app.presentation.telegram.view.models import View


@dataclass(frozen=True)
class ProfilePresenter(BasePresenter):
    def profile(self, user: User) -> View:
        # TODO(M1): localized enum titles instead of raw values
        return View(
            text=self.i18n.messages.profile(
                name=user.mention,
                native_language=user.native_language or "—",
                level=user.english_level or "—",
                goal=user.learning_goal or "—",
                format=user.communication_format or "—",
                plan=user.subscription_type,
            ),
            edit=False,
        )

    def settings(self) -> View:
        return View(
            text=self.i18n.messages.settings(),
            reply_markup=settings_keyboard(i18n=self.i18n),
            edit=False,
        )
