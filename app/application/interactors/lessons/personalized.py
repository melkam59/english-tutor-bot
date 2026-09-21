from dataclasses import dataclass
from typing import Optional

from app.application.interactors.base import BaseInteractor
from app.application.ports.llm.gateway import LLMGateway
from app.application.ports.repositories.lessons import LessonsGateway
from app.application.ports.repositories.mistakes import MistakesGateway
from app.application.ports.repositories.vocabulary import VocabularyGateway
from app.application.services.access import AccessPolicy
from app.application.services.prompts import PromptBuilder
from app.domain.lesson import Lesson
from app.domain.user import User


@dataclass(frozen=True)
class LessonsInteractor(BaseInteractor):
    user: User
    llm: LLMGateway
    prompts: PromptBuilder
    access: AccessPolicy
    lessons_gateway: LessonsGateway
    mistakes_gateway: MistakesGateway
    vocabulary_gateway: VocabularyGateway

    async def generate(self, topic: Optional[str] = None) -> Lesson:
        # TODO(M3): explanation + examples + exercise based on level, goal,
        #  previous mistakes and recently learned vocabulary
        raise NotImplementedError

    async def submit_answer(self, lesson_id: int, answer: str) -> Lesson:
        # TODO(M3): AI feedback + additional practice question, mark as completed
        raise NotImplementedError
