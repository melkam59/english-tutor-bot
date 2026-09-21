from typing import Any, Final

from aiogram import Router
from aiogram.filters import ExceptionTypeFilter
from aiogram.types import ErrorEvent
from dishka import FromDishka

from app.application.errors.base import AppError
from app.application.errors.limits import LimitError
from app.application.errors.llm import LLMError
from app.application.errors.speech import SpeechError
from app.presentation.telegram.flows.extra.errors import ExtraErrorsFlow

router: Final[Router] = Router(name=__name__)


@router.error(ExceptionTypeFilter(LimitError))
async def handle_limit_error(event: ErrorEvent, flow: FromDishka[ExtraErrorsFlow]) -> Any:
    await flow.answer_limit_error(error=event.exception)  # type: ignore[arg-type]


@router.error(ExceptionTypeFilter(LLMError))
async def handle_llm_error(_: ErrorEvent, flow: FromDishka[ExtraErrorsFlow]) -> Any:
    await flow.answer_llm_error()


@router.error(ExceptionTypeFilter(SpeechError))
async def handle_speech_error(_: ErrorEvent, flow: FromDishka[ExtraErrorsFlow]) -> Any:
    await flow.answer_speech_error()


@router.error(ExceptionTypeFilter(AppError))
async def handle_some_error(_: ErrorEvent, flow: FromDishka[ExtraErrorsFlow]) -> Any:
    await flow.answer_something_went_wrong()


# TODO(M5): catch-all for unexpected exceptions (log with traceback, never leak details
#  to the user, forward to Sentry when COMMON_SENTRY_DSN is set)
