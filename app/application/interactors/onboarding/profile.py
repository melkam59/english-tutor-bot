from dataclasses import dataclass

from app.application.errors.profile import ProfileIncompleteError
from app.application.interactors.base import BaseInteractor
from app.application.ports.repositories.users import UsersGateway
from app.domain.enums.communication_format import CommunicationFormat
from app.domain.enums.english_level import EnglishLevel
from app.domain.enums.learning_goal import LearningGoal
from app.domain.user import User
from app.utils.time import datetime_now


@dataclass(frozen=True)
class ProfileInteractor(BaseInteractor):
    """User registration follow-up: learning profile setup and /settings changes."""

    user: User
    users_gateway: UsersGateway

    async def complete_onboarding(self) -> None:
        answers = (
            self.user.native_language,
            self.user.english_level,
            self.user.learning_goal,
            self.user.communication_format,
        )
        if any(answer is None for answer in answers):
            raise ProfileIncompleteError()
        self.user.onboarded_at = datetime_now()
        await self.users_gateway.save(self.user)

    async def set_native_language(self, language: str) -> None:
        self.user.native_language = language
        await self.users_gateway.save(self.user)

    async def set_english_level(self, level: EnglishLevel) -> None:
        self.user.english_level = level
        await self.users_gateway.save(self.user)

    async def set_learning_goal(self, goal: LearningGoal) -> None:
        self.user.learning_goal = goal
        await self.users_gateway.save(self.user)

    async def set_communication_format(self, communication_format: CommunicationFormat) -> None:
        self.user.communication_format = communication_format
        await self.users_gateway.save(self.user)
