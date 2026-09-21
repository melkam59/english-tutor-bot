from dataclasses import dataclass

from app.application.interactors.base import BaseInteractor
from app.application.ports.llm.gateway import LLMGateway
from app.application.ports.repositories.vocabulary import VocabularyGateway
from app.application.services.access import AccessPolicy
from app.application.services.prompts import PromptBuilder
from app.domain.user import User
from app.domain.vocabulary_item import VocabularyItem


@dataclass(frozen=True)
class VocabularyInteractor(BaseInteractor):
    user: User
    llm: LLMGateway
    prompts: PromptBuilder
    access: AccessPolicy
    vocabulary_gateway: VocabularyGateway

    async def add(self, phrase: str) -> VocabularyItem:
        # TODO(M3): the LLM provides translation + example sentence
        raise NotImplementedError

    async def remove(self, item_id: int) -> None:
        # TODO(M3)
        raise NotImplementedError

    async def get_page(self, page: int) -> list[VocabularyItem]:
        # TODO(M3)
        raise NotImplementedError

    async def get_due(self) -> list[VocabularyItem]:
        # TODO(M3)
        raise NotImplementedError

    async def answer_review(self, item_id: int, is_correct: bool) -> VocabularyItem:
        # TODO(M3): update counters, services.spaced_repetition.schedule_next_review
        raise NotImplementedError
