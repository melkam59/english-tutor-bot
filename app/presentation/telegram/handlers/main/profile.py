from typing import Any, Final

from aiogram import Router
from aiogram.filters import Command
from aiogram.types import CallbackQuery, Message
from dishka import FromDishka

from app.presentation.telegram.callbacks.settings import CDSettings
from app.presentation.telegram.flows.common.profile import ProfileFlow

router: Final[Router] = Router(name=__name__)


@router.message(Command("profile"))
async def show_profile(_: Message, flow: FromDishka[ProfileFlow]) -> Any:
    return await flow.show_profile()


@router.message(Command("settings"))
async def show_settings(_: Message, flow: FromDishka[ProfileFlow]) -> Any:
    return await flow.show_settings()


@router.callback_query(CDSettings.filter())
async def edit_field(
    _: CallbackQuery,
    callback_data: CDSettings,
    flow: FromDishka[ProfileFlow],
) -> Any:
    return await flow.edit_field(field=callback_data.field)
