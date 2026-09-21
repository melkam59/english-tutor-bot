from dataclasses import dataclass

from app.domain.user import User
from app.presentation.telegram.keyboards.onboarding import (
    communication_format_keyboard,
    english_level_keyboard,
    learning_goal_keyboard,
    native_language_keyboard,
)
from app.presentation.telegram.presenters.base import BasePresenter
from app.presentation.telegram.view.models import View


@dataclass(frozen=True)
class OnboardingPresenter(BasePresenter):
    def ask_native_language(self, user: User) -> View:
        return View(
            text=self.i18n.messages.onboarding.native_language(name=user.mention),
            reply_markup=native_language_keyboard(),
        )

    def ask_english_level(self) -> View:
        return View(
            text=self.i18n.messages.onboarding.english_level(),
            reply_markup=english_level_keyboard(i18n=self.i18n),
        )

    def ask_learning_goal(self) -> View:
        return View(
            text=self.i18n.messages.onboarding.learning_goal(),
            reply_markup=learning_goal_keyboard(i18n=self.i18n),
        )

    def ask_communication_format(self) -> View:
        return View(
            text=self.i18n.messages.onboarding.communication_format(),
            reply_markup=communication_format_keyboard(i18n=self.i18n),
        )

    def completed(self) -> View:
        return View(text=self.i18n.messages.onboarding.completed())

    # TODO(M3): offer_assessment / question / result screens
