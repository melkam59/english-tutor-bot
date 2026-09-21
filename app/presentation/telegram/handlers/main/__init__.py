from typing import Final

from aiogram import F, Router
from aiogram.enums import ChatType

from . import (
    chat,
    lesson,
    onboarding,
    practice,
    profile,
    progress,
    start,
    subscription,
    vocabulary,
)

router: Final[Router] = Router(name=__name__)
router.message.filter(F.chat.type == ChatType.PRIVATE)
router.include_routers(
    start.router,
    onboarding.router,
    profile.router,
    practice.router,
    lesson.router,
    vocabulary.router,
    progress.router,
    subscription.router,
    chat.router,
)
