from typing import Any, Final

from aiogram import Router
from aiogram.filters import Command
from aiogram.types import CallbackQuery, Message
from dishka import FromDishka

from app.presentation.telegram.callbacks.practice import (
    CDPracticeMode,
    CDRolePlayScenario,
    CDStopPractice,
)
from app.presentation.telegram.flows.common.practice import PracticeFlow

router: Final[Router] = Router(name=__name__)


@router.message(Command("practice"))
async def choose_mode(_: Message, flow: FromDishka[PracticeFlow]) -> Any:
    return await flow.choose_mode()


@router.callback_query(CDPracticeMode.filter())
async def select_mode(
    _: CallbackQuery,
    callback_data: CDPracticeMode,
    flow: FromDishka[PracticeFlow],
) -> Any:
    return await flow.select_mode(mode=callback_data.mode)


@router.callback_query(CDRolePlayScenario.filter())
async def select_scenario(
    _: CallbackQuery,
    callback_data: CDRolePlayScenario,
    flow: FromDishka[PracticeFlow],
) -> Any:
    return await flow.select_scenario(scenario=callback_data.scenario)


@router.callback_query(CDStopPractice.filter())
async def stop_practice(_: CallbackQuery, flow: FromDishka[PracticeFlow]) -> Any:
    return await flow.stop()
