from enum import StrEnum, auto

from aiogram.filters.callback_data import CallbackData


# noinspection PyEnum
class SettingsField(StrEnum):
    NATIVE_LANGUAGE = auto()
    ENGLISH_LEVEL = auto()
    LEARNING_GOAL = auto()
    COMMUNICATION_FORMAT = auto()
    RETAKE_ASSESSMENT = auto()


class CDSettings(CallbackData, prefix="settings"):
    field: SettingsField
