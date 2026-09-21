from dataclasses import dataclass

from app.presentation.telegram.presenters.base import BasePresenter
from app.presentation.telegram.view.models import View


@dataclass(frozen=True)
class ExtraErrorsPresenter(BasePresenter):
    def something_went_wrong(self) -> View:
        return View(text=self.i18n.messages.errors.something_went_wrong())

    def daily_limit_reached(self) -> View:
        return View(text=self.i18n.messages.errors.daily_limit_reached(), edit=False)

    def voice_limit_reached(self) -> View:
        return View(text=self.i18n.messages.errors.voice_limit_reached(), edit=False)

    def voice_too_long(self) -> View:
        return View(text=self.i18n.messages.errors.voice_too_long(), edit=False)

    def input_too_long(self) -> View:
        return View(text=self.i18n.messages.errors.input_too_long(), edit=False)

    def premium_required(self) -> View:
        return View(text=self.i18n.messages.errors.premium_required(), edit=False)

    def llm_unavailable(self) -> View:
        return View(text=self.i18n.messages.errors.llm_unavailable(), edit=False)

    def voice_not_recognized(self) -> View:
        return View(text=self.i18n.messages.errors.voice_not_recognized(), edit=False)
