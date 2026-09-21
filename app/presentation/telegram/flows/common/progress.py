from dataclasses import dataclass
from typing import Any

from app.application.interactors.progress.summary import ProgressInteractor
from app.presentation.telegram.flows.base import BaseFlow
from app.presentation.telegram.presenters.common.progress import ProgressPresenter
from app.presentation.telegram.view.renderer import Renderer


@dataclass(frozen=True)
class ProgressFlow(BaseFlow):
    interactor: ProgressInteractor
    presenter: ProgressPresenter
    renderer: Renderer

    async def show_summary(self) -> Any:
        # TODO(M3): interactor.get_summary -> presenter.summary
        return await self.renderer.apply(self.presenter.not_implemented())
