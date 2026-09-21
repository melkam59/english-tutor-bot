from typing import Any, Final

from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import CallbackQuery, Message
from dishka import FromDishka

from app.presentation.telegram.callbacks.vocabulary import (
    CDVocabularyAdd,
    CDVocabularyAnswer,
    CDVocabularyDelete,
    CDVocabularyList,
    CDVocabularyReview,
)
from app.presentation.telegram.flows.common.vocabulary import VocabularyFlow
from app.presentation.telegram.states import VocabularySG

router: Final[Router] = Router(name=__name__)


@router.message(Command("vocabulary"))
async def vocabulary_menu(_: Message, flow: FromDishka[VocabularyFlow]) -> Any:
    return await flow.menu()


@router.callback_query(CDVocabularyAdd.filter())
async def ask_phrase(_: CallbackQuery, flow: FromDishka[VocabularyFlow]) -> Any:
    return await flow.ask_phrase()


@router.message(VocabularySG.waiting_phrase, F.text)
async def add_phrase(message: Message, flow: FromDishka[VocabularyFlow]) -> Any:
    return await flow.add_phrase(phrase=message.text)


@router.callback_query(CDVocabularyList.filter())
async def show_page(
    _: CallbackQuery,
    callback_data: CDVocabularyList,
    flow: FromDishka[VocabularyFlow],
) -> Any:
    return await flow.show_page(page=callback_data.page)


@router.callback_query(CDVocabularyDelete.filter())
async def delete_item(
    _: CallbackQuery,
    callback_data: CDVocabularyDelete,
    flow: FromDishka[VocabularyFlow],
) -> Any:
    return await flow.delete_item(item_id=callback_data.item_id)


@router.callback_query(CDVocabularyReview.filter())
async def start_review(_: CallbackQuery, flow: FromDishka[VocabularyFlow]) -> Any:
    return await flow.start_review()


@router.callback_query(CDVocabularyAnswer.filter())
async def answer_review(
    _: CallbackQuery,
    callback_data: CDVocabularyAnswer,
    flow: FromDishka[VocabularyFlow],
) -> Any:
    return await flow.answer_review(
        item_id=callback_data.item_id,
        is_correct=callback_data.is_correct,
    )
