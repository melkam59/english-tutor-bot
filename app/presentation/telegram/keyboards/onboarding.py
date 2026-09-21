from typing import Final

from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram_i18n import I18nContext

from app.domain.enums.communication_format import CommunicationFormat
from app.domain.enums.english_level import EnglishLevel
from app.domain.enums.learning_goal import LearningGoal
from app.domain.enums.locale import Locale
from app.presentation.telegram.callbacks.onboarding import (
    CDCommunicationFormat,
    CDEnglishLevel,
    CDLearningGoal,
    CDNativeLanguage,
)

# Languages the tutor can explain corrections in
NATIVE_LANGUAGES: Final[dict[Locale, str]] = {
    Locale.UK: "🇺🇦 Українська",
    Locale.PL: "🇵🇱 Polski",
    Locale.RU: "Русский",
    Locale.DE: "🇩🇪 Deutsch",
    Locale.ES: "🇪🇸 Español",
    Locale.FR: "🇫🇷 Français",
    Locale.IT: "🇮🇹 Italiano",
    Locale.PT: "🇵🇹 Português",
    Locale.TR: "🇹🇷 Türkçe",
    Locale.AR: "العربية",
}


def native_language_keyboard() -> InlineKeyboardMarkup:
    builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
    for locale, title in NATIVE_LANGUAGES.items():
        builder.button(text=title, callback_data=CDNativeLanguage(code=locale.value))
    builder.adjust(2)
    return builder.as_markup()


def english_level_keyboard(i18n: I18nContext) -> InlineKeyboardMarkup:
    builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
    for level in EnglishLevel:
        builder.button(
            text=i18n.get(f"buttons-level-{level.value.lower()}"),
            callback_data=CDEnglishLevel(level=level),
        )
    builder.adjust(1)
    return builder.as_markup()


def learning_goal_keyboard(i18n: I18nContext) -> InlineKeyboardMarkup:
    builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
    for goal in LearningGoal:
        builder.button(
            text=i18n.get(f"buttons-goal-{goal.value}"),
            callback_data=CDLearningGoal(goal=goal),
        )
    builder.adjust(2)
    return builder.as_markup()


def communication_format_keyboard(i18n: I18nContext) -> InlineKeyboardMarkup:
    builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
    for communication_format in CommunicationFormat:
        builder.button(
            text=i18n.get(f"buttons-format-{communication_format.value}"),
            callback_data=CDCommunicationFormat(format=communication_format),
        )
    builder.adjust(1)
    return builder.as_markup()
