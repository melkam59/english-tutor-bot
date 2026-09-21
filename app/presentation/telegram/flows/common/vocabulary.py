from dataclasses import dataclass
from typing import Any

from app.application.interactors.vocabulary.trainer import VocabularyInteractor
from app.presentation.telegram.flows.base import BaseFlow
from app.presentation.telegram.presenters.common.vocabulary import VocabularyPresenter
from app.presentation.telegram.view.renderer import Renderer


@dataclass(frozen=True)
class VocabularyFlow(BaseFlow):
    interactor: VocabularyInteractor
    presenter: VocabularyPresenter
    renderer: Renderer

    async def menu(self) -> Any:
        return await self.renderer.apply(self.presenter.menu())

    async def ask_phrase(self) -> Any:
        # TODO(M3): set VocabularySG.waiting_phrase
        return await self.renderer.apply(self.presenter.not_implemented())

    async def add_phrase(self, phrase: str) -> Any:
        # TODO(M3)
        return await self.renderer.apply(self.presenter.not_implemented())

    async def show_page(self, page: int) -> Any:
        # TODO(M3)
        return await self.renderer.apply(self.presenter.not_implemented())

    async def delete_item(self, item_id: int) -> Any:
        # TODO(M3)
        return await self.renderer.apply(self.presenter.not_implemented())

    async def start_review(self) -> Any:
        # TODO(M3)
        return await self.renderer.apply(self.presenter.not_implemented())

    async def answer_review(self, item_id: int, is_correct: bool) -> Any:
        # TODO(M3)
        return await self.renderer.apply(self.presenter.not_implemented())
