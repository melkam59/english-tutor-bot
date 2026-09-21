from typing import Optional

from app.application.models.state.base import StateModel
from app.domain.enums.communication_format import CommunicationFormat
from app.domain.enums.english_level import EnglishLevel
from app.domain.enums.learning_goal import LearningGoal


class OnboardingState(StateModel):
    native_language: Optional[str] = None
    english_level: Optional[EnglishLevel] = None
    learning_goal: Optional[LearningGoal] = None
    communication_format: Optional[CommunicationFormat] = None
