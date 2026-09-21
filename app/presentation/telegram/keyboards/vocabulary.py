from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram_i18n import I18nContext

from app.presentation.telegram.callbacks.vocabulary import (
    CDVocabularyAdd,
    CDVocabularyList,
    CDVocabularyReview,
)


def vocabulary_menu_keyboard(i18n: I18nContext) -> InlineKeyboardMarkup:
    builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
    builder.button(text=i18n.buttons.vocabulary.add(), callback_data=CDVocabularyAdd())
    builder.button(text=i18n.buttons.vocabulary.list(), callback_data=CDVocabularyList())
    builder.button(text=i18n.buttons.vocabulary.review(), callback_data=CDVocabularyReview())
    builder.adjust(1)
    return builder.as_markup()
