from typing import Any, Final

from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import Message, TelegramObject
from dishka import FromDishka

from app.presentation.telegram.callbacks.lesson import CDNewLesson
from app.presentation.telegram.flows.common.lesson import LessonFlow
from app.presentation.telegram.states import LessonSG

router: Final[Router] = Router(name=__name__)


@router.message(Command("lesson"))
@router.callback_query(CDNewLesson.filter())
async def new_lesson(_: TelegramObject, flow: FromDishka[LessonFlow]) -> Any:
    return await flow.new_lesson()


@router.message(LessonSG.waiting_answer, F.text)
async def submit_answer(message: Message, flow: FromDishka[LessonFlow]) -> Any:
    return await flow.submit_answer(text=message.text)
