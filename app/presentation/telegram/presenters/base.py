from abc import ABC
from dataclasses import dataclass

from aiogram_i18n import I18nContext

from app.presentation.telegram.view.models import View


@dataclass(frozen=True)
class BasePresenter(ABC):
    i18n: I18nContext

    def not_implemented(self) -> View:
        """Scaffold placeholder, remove once every screen is implemented."""
        return View(text=self.i18n.messages.not_implemented(), edit=False)
