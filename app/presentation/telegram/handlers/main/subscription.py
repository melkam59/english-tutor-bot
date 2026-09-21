from typing import Any, Final

from aiogram import Router
from aiogram.filters import Command
from aiogram.types import CallbackQuery, Message
from dishka import FromDishka

from app.presentation.telegram.callbacks.subscription import CDBuyPremium
from app.presentation.telegram.flows.common.subscription import SubscriptionFlow

router: Final[Router] = Router(name=__name__)


@router.message(Command("subscription"))
async def show_plans(_: Message, flow: FromDishka[SubscriptionFlow]) -> Any:
    return await flow.show_plans()


@router.callback_query(CDBuyPremium.filter())
async def buy_premium(
    _: CallbackQuery,
    callback_data: CDBuyPremium,
    flow: FromDishka[SubscriptionFlow],
) -> Any:
    return await flow.buy_premium(months=callback_data.months)
