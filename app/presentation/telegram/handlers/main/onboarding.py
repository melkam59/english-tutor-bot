from typing import Any, Final

from aiogram import F, Router
from aiogram.types import CallbackQuery, Message
from dishka import FromDishka

from app.presentation.telegram.callbacks.assessment import (
    CDAssessmentAnswer,
    CDSkipAssessment,
    CDStartAssessment,
)
from app.presentation.telegram.callbacks.onboarding import (
    CDCommunicationFormat,
    CDEnglishLevel,
    CDLearningGoal,
    CDNativeLanguage,
)
from app.presentation.telegram.flows.common.onboarding import OnboardingFlow
from app.presentation.telegram.states import AssessmentSG

router: Final[Router] = Router(name=__name__)


@router.callback_query(CDNativeLanguage.filter())
async def select_native_language(
    _: CallbackQuery,
    callback_data: CDNativeLanguage,
    flow: FromDishka[OnboardingFlow],
) -> Any:
    return await flow.select_native_language(code=callback_data.code)


@router.callback_query(CDEnglishLevel.filter())
async def select_english_level(
    _: CallbackQuery,
    callback_data: CDEnglishLevel,
    flow: FromDishka[OnboardingFlow],
) -> Any:
    return await flow.select_english_level(level=callback_data.level)


@router.callback_query(CDLearningGoal.filter())
async def select_learning_goal(
    _: CallbackQuery,
    callback_data: CDLearningGoal,
    flow: FromDishka[OnboardingFlow],
) -> Any:
    return await flow.select_learning_goal(goal=callback_data.goal)


@router.callback_query(CDCommunicationFormat.filter())
async def select_communication_format(
    _: CallbackQuery,
    callback_data: CDCommunicationFormat,
    flow: FromDishka[OnboardingFlow],
) -> Any:
    return await flow.select_communication_format(communication_format=callback_data.format)


@router.callback_query(CDStartAssessment.filter())
async def start_assessment(_: CallbackQuery, flow: FromDishka[OnboardingFlow]) -> Any:
    return await flow.start_assessment()


@router.callback_query(CDSkipAssessment.filter())
async def skip_assessment(_: CallbackQuery, flow: FromDishka[OnboardingFlow]) -> Any:
    return await flow.skip_assessment()


@router.callback_query(CDAssessmentAnswer.filter(), AssessmentSG.multiple_choice)
async def answer_question(
    _: CallbackQuery,
    callback_data: CDAssessmentAnswer,
    flow: FromDishka[OnboardingFlow],
) -> Any:
    return await flow.answer_question(
        question_id=callback_data.question_id,
        option=callback_data.option,
    )


@router.message(AssessmentSG.written_answer, F.text)
async def answer_written_question(message: Message, flow: FromDishka[OnboardingFlow]) -> Any:
    return await flow.answer_written_question(text=message.text)
