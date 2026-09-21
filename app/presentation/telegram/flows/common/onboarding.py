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
    Intermediate answers live in FSM data (``OnboardingState`` / ``AssessmentState``).
    """

    profile: ProfileInteractor
    assessment: LevelAssessmentInteractor
    presenter: OnboardingPresenter
    renderer: Renderer

    async def select_native_language(self, code: str) -> Any:
        # TODO(M1): store in OnboardingState, render ask_english_level
        return await self.renderer.apply(self.presenter.not_implemented())

    async def select_english_level(self, level: EnglishLevel) -> Any:
        # TODO(M1)
        return await self.renderer.apply(self.presenter.not_implemented())

    async def select_learning_goal(self, goal: LearningGoal) -> Any:
        # TODO(M1)
        return await self.renderer.apply(self.presenter.not_implemented())

    async def select_communication_format(self, communication_format: CommunicationFormat) -> Any:
        # TODO(M1): profile.complete_onboarding, then offer the assessment
        return await self.renderer.apply(self.presenter.not_implemented())

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
