from aiogram.filters.callback_data import CallbackData

from app.domain.enums.communication_format import CommunicationFormat
from app.domain.enums.english_level import EnglishLevel
from app.domain.enums.learning_goal import LearningGoal


class CDNativeLanguage(CallbackData, prefix="native_lang"):
    code: str


class CDEnglishLevel(CallbackData, prefix="level"):
    level: EnglishLevel


class CDLearningGoal(CallbackData, prefix="goal"):
    goal: LearningGoal


class CDCommunicationFormat(CallbackData, prefix="format"):
    format: CommunicationFormat
