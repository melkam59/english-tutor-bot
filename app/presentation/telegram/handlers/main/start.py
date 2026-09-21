from typing import Any, Final

from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.types import TelegramObject
from dishka import FromDishka

from app.presentation.telegram.callbacks.menu import CDMenu
from app.presentation.telegram.flows.common.menu import CommonMenuFlow

router: Final[Router] = Router(name=__name__)


@router.message(CommandStart())
@router.callback_query(CDMenu.filter())
async def start(_: TelegramObject, flow: FromDishka[CommonMenuFlow]) -> Any:
    return await flow.start()


@router.message(Command("help"))
async def help_command(_: TelegramObject, flow: FromDishka[CommonMenuFlow]) -> Any:
    return await flow.help()
