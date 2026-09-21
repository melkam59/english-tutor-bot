from dataclasses import dataclass
from typing import Any

from app.application.interactors.lessons.personalized import LessonsInteractor
from app.application.interactors.limits.usage import UsageLimitsInteractor
from app.presentation.telegram.flows.base import BaseFlow
from app.presentation.telegram.presenters.common.lesson import LessonPresenter
from app.presentation.telegram.view.renderer import Renderer


@dataclass(frozen=True)
class LessonFlow(BaseFlow):
    interactor: LessonsInteractor
    limits: UsageLimitsInteractor
    presenter: LessonPresenter
    renderer: Renderer

    async def new_lesson(self) -> Any:
        # TODO(M3): interactor.generate, set LessonSG.waiting_answer
        return await self.renderer.apply(self.presenter.not_implemented())

    async def submit_answer(self, text: str) -> Any:
        # TODO(M3)
        return await self.renderer.apply(self.presenter.not_implemented())
