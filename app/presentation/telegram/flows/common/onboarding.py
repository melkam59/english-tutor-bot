from dataclasses import dataclass
from typing import Any

from app.application.interactors.assessment.level_assessment import LevelAssessmentInteractor
from app.application.interactors.onboarding.profile import ProfileInteractor
from app.domain.enums.communication_format import CommunicationFormat
from app.domain.enums.english_level import EnglishLevel
from app.domain.enums.learning_goal import LearningGoal
from app.presentation.telegram.flows.base import BaseFlow
from app.presentation.telegram.presenters.common.onboarding import OnboardingPresenter
from app.presentation.telegram.view.renderer import Renderer


@dataclass(frozen=True)
class OnboardingFlow(BaseFlow):
    """
    /start -> native language -> English level -> goal -> format -> assessment -> profile.
    Every answer is saved to the user right away, assessment answers live in FSM data.
    """

    profile: ProfileInteractor
    assessment: LevelAssessmentInteractor
    presenter: OnboardingPresenter
    renderer: Renderer

    async def select_native_language(self, code: str) -> Any:
        await self.profile.set_native_language(code)
        return await self.renderer.apply(self.presenter.ask_english_level())

    async def select_english_level(self, level: EnglishLevel) -> Any:
        await self.profile.set_english_level(level)
        return await self.renderer.apply(self.presenter.ask_learning_goal())

    async def select_learning_goal(self, goal: LearningGoal) -> Any:
        await self.profile.set_learning_goal(goal)
        return await self.renderer.apply(self.presenter.ask_communication_format())

    async def select_communication_format(self, communication_format: CommunicationFormat) -> Any:
        await self.profile.set_communication_format(communication_format)
        await self.profile.complete_onboarding()
        # TODO(M3): offer the level assessment before the first conversation
        return await self.renderer.apply(self.presenter.completed())

    async def start_assessment(self) -> Any:
        # TODO(M3)
        return await self.renderer.apply(self.presenter.not_implemented())

    async def skip_assessment(self) -> Any:
        # TODO(M3): keep the self-reported level
        return await self.renderer.apply(self.presenter.not_implemented())

    async def answer_question(self, question_id: int, option: int) -> Any:
        # TODO(M3)
        return await self.renderer.apply(self.presenter.not_implemented())

    async def answer_written_question(self, text: str) -> Any:
        # TODO(M3): assessment.finish -> result screen
        return await self.renderer.apply(self.presenter.not_implemented())
