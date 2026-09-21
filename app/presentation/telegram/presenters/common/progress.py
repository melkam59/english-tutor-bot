from dataclasses import dataclass

from app.application.models.dto.progress import ProgressSummary
from app.presentation.telegram.presenters.base import BasePresenter
from app.presentation.telegram.view.models import View


@dataclass(frozen=True)
class ProgressPresenter(BasePresenter):
    def summary(self, summary: ProgressSummary) -> View:
        # TODO(M3)
        raise NotImplementedError
