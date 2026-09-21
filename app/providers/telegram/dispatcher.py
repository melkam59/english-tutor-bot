from __future__ import annotations

from aiogram import Dispatcher
from aiogram.fsm.storage.redis import RedisStorage
from aiogram.utils.callback_answer import CallbackAnswerMiddleware
from dishka import AsyncContainer
from dishka.integrations.aiogram import setup_dishka

from app.presentation.telegram.handlers import admin, extra, main
from app.presentation.telegram.middlewares.ban import BanMiddleware
from app.presentation.telegram.middlewares.container import UpdateContainerContextMiddleware
from app.presentation.telegram.middlewares.logging import UpdateLoggingMiddleware
from app.presentation.telegram.middlewares.throttling import (
    ThrottlingMiddleware,
    UpdateDedupMiddleware,
)


async def create_dispatcher(container: AsyncContainer) -> Dispatcher:
    """
    :return: Configured ``Dispatcher`` with installed middlewares and included routers
    """
    fsm_storage: RedisStorage = await container.get(RedisStorage)

    # noinspection PyArgumentList
    dispatcher: Dispatcher = Dispatcher(name="main_dispatcher", storage=fsm_storage)
    dispatcher.include_routers(admin.router, main.router, extra.router)
    setup_dishka(container=container, router=dispatcher, auto_inject=True)
    dispatcher.update.outer_middleware(UpdateContainerContextMiddleware())
    UpdateLoggingMiddleware().setup_outer(router=dispatcher)
    UpdateDedupMiddleware().setup_outer(router=dispatcher)
    ThrottlingMiddleware().setup_outer(router=dispatcher)
    BanMiddleware().setup_inner(router=dispatcher)
    dispatcher.callback_query.middleware(CallbackAnswerMiddleware())

    return dispatcher
