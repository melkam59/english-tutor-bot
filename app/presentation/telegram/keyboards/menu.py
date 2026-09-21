from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram_i18n import I18nContext

from app.domain.enums.practice_mode import PracticeMode
from app.presentation.telegram.callbacks.practice import CDPracticeMode, CDStopPractice
from app.presentation.telegram.callbacks.subscription import CDBuyPremium


def practice_modes_keyboard(i18n: I18nContext) -> InlineKeyboardMarkup:
    builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
    for mode in PracticeMode:
        builder.button(
            text=i18n.get(f"buttons-practice-{mode.value}"),
            callback_data=CDPracticeMode(mode=mode),
        )
    # TODO(M4): mark premium-only modes with a lock for free users
    builder.adjust(2)
    return builder.as_markup()


def stop_practice_keyboard(i18n: I18nContext) -> InlineKeyboardMarkup:
    builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
    builder.button(text=i18n.buttons.practice.stop(), callback_data=CDStopPractice())
    return builder.as_markup()


def subscription_keyboard(i18n: I18nContext) -> InlineKeyboardMarkup:
    builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
    builder.button(text=i18n.buttons.subscription.buy(), callback_data=CDBuyPremium())
    return builder.as_markup()
