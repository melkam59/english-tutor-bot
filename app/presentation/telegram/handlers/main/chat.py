from typing import Any, Final

from aiogram import F, Router
from aiogram.types import Message
from dishka import FromDishka

from app.presentation.telegram.filters.states import NoneState
from app.presentation.telegram.flows.common.practice import PracticeFlow

# Catch-all AI tutor conversation, must stay the LAST router in handlers/main/__init__.py
router: Final[Router] = Router(name=__name__)
router.message.filter(NoneState)


@router.message(F.text & ~F.text.startswith("/"))
async def reply_text(message: Message, flow: FromDishka[PracticeFlow]) -> Any:
    return await flow.reply_text(text=message.text)


@router.message(F.voice)
async def reply_voice(message: Message, flow: FromDishka[PracticeFlow]) -> Any:
    return await flow.reply_voice(
        file_id=message.voice.file_id,
        duration=message.voice.duration,
    )
