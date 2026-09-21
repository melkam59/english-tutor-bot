from dataclasses import dataclass

from app.application.models.dto.admin import AdminStats, BroadcastResult
from app.presentation.telegram.presenters.base import BasePresenter
from app.presentation.telegram.view.models import View


@dataclass(frozen=True)
class AdminPresenter(BasePresenter):
    def stats(self, stats: AdminStats) -> View:
        # TODO(M4)
        raise NotImplementedError

    def broadcast_result(self, result: BroadcastResult) -> View:
        # TODO(M4)
        raise NotImplementedError

    def done(self) -> View:
        return View(text=self.i18n.messages.admin.done(), edit=False)

    def invalid_arguments(self) -> View:
        return View(text=self.i18n.messages.admin.invalid_arguments(), edit=False)
