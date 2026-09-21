from dataclasses import dataclass

from app.domain.vocabulary_item import VocabularyItem
from app.presentation.telegram.keyboards.vocabulary import vocabulary_menu_keyboard
from app.presentation.telegram.presenters.base import BasePresenter
from app.presentation.telegram.view.models import View


@dataclass(frozen=True)
class VocabularyPresenter(BasePresenter):
    def menu(self) -> View:
        return View(
            text=self.i18n.messages.vocabulary.menu(),
            reply_markup=vocabulary_menu_keyboard(i18n=self.i18n),
            edit=False,
        )

    def items_page(self, items: list[VocabularyItem], page: int) -> View:
        # TODO(M3)
        raise NotImplementedError

    def review_card(self, item: VocabularyItem) -> View:
        # TODO(M3)
        raise NotImplementedError
