from dataclasses import dataclass

from app.application.interactors.base import BaseInteractor
from app.application.models.state.onboarding import OnboardingState
from app.application.ports.repositories.users import UsersGateway
from app.domain.enums.communication_format import CommunicationFormat
from app.domain.enums.english_level import EnglishLevel
from app.domain.enums.learning_goal import LearningGoal
from app.domain.user import User


@dataclass(frozen=True)
class ProfileInteractor(BaseInteractor):
    """User registration follow-up: learning profile setup and /settings changes."""

    user: User
    users_gateway: UsersGateway

    async def complete_onboarding(self, state: OnboardingState) -> None:
        # TODO(M1): validate that every field is filled, persist, set onboarded_at
        raise NotImplementedError

    async def set_native_language(self, language: str) -> None:
        # TODO(M1)
        raise NotImplementedError

    async def set_english_level(self, level: EnglishLevel) -> None:
        # TODO(M1)
        raise NotImplementedError

    async def set_learning_goal(self, goal: LearningGoal) -> None:
        # TODO(M1)
        raise NotImplementedError

    async def set_communication_format(self, communication_format: CommunicationFormat) -> None:
        # TODO(M1)
        raise NotImplementedError
