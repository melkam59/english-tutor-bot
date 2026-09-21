from dataclasses import dataclass

from app.domain.lesson import Lesson
from app.presentation.telegram.presenters.base import BasePresenter
from app.presentation.telegram.view.models import View


@dataclass(frozen=True)
class LessonPresenter(BasePresenter):
    def lesson(self, lesson: Lesson) -> View:
        # TODO(M3): explanation, examples and the exercise
        raise NotImplementedError

    def feedback(self, lesson: Lesson) -> View:
        # TODO(M3): AI feedback + additional practice question
        raise NotImplementedError
