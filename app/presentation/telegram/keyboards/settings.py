from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram_i18n import I18nContext

from app.presentation.telegram.callbacks.settings import CDSettings, SettingsField


def settings_keyboard(i18n: I18nContext) -> InlineKeyboardMarkup:
    builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
    for field in SettingsField:
        builder.button(
            text=i18n.get(f"buttons-settings-{field.value}"),
            callback_data=CDSettings(field=field),
        )
    builder.adjust(1)
    return builder.as_markup()
