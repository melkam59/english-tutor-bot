from typing import Final

from aiogram import Router

from app.presentation.telegram.filters import ADMIN_FILTER

from . import panel

router: Final[Router] = Router(name=__name__)
router.message.filter(ADMIN_FILTER)
router.callback_query.filter(ADMIN_FILTER)
router.include_routers(panel.router)
