from typing import Any, Final

from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from dishka import FromDishka

from app.presentation.telegram.flows.common.progress import ProgressFlow

router: Final[Router] = Router(name=__name__)


@router.message(Command("progress"))
async def show_progress(_: Message, flow: FromDishka[ProgressFlow]) -> Any:
    return await flow.show_summary()
