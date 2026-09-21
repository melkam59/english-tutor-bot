from dataclasses import dataclass
from typing import Optional

from app.domain.conversation import Conversation
from app.domain.enums.english_level import EnglishLevel
from app.domain.user import User
from app.domain.user_mistake import UserMistake
from app.domain.vocabulary_item import VocabularyItem
from app.utils.custom_types import DictStrAny


@dataclass(frozen=True)
class PromptBuilder:
    """
    Single place where prompts are assembled. Prompt templates are kept in
    ``assets/prompts/*.md`` so they can be edited without touching the code.
    """

    def tutor_system_prompt(
        self,
        user: User,
        conversation: Conversation,
        recent_mistakes: list[UserMistake],
    ) -> str:
        # TODO(M2): user level, native language, goal, mode/scenario, recent mistakes, summary
        raise NotImplementedError

    def tutor_reply_schema(self) -> DictStrAny:
        # TODO(M2): JSON schema matching app.application.models.dto.llm.TutorReply
        raise NotImplementedError

    def summary_prompt(self, previous_summary: Optional[str]) -> str:
        # TODO(M2)
        raise NotImplementedError

    def lesson_prompt(
        self,
        user: User,
        topic: Optional[str],
        recent_mistakes: list[UserMistake],
        recent_vocabulary: list[VocabularyItem],
    ) -> str:
        # TODO(M3)
        raise NotImplementedError

    def lesson_feedback_prompt(self, user: User, exercise: str, answer: str) -> str:
        # TODO(M3)
        raise NotImplementedError

    def vocabulary_card_prompt(self, user: User, phrase: str) -> str:
        # TODO(M3): translation into the native language + example sentence
        raise NotImplementedError

    def assessment_writing_prompt(self, claimed_level: Optional[EnglishLevel]) -> str:
        # TODO(M3): grade a short written answer on the CEFR scale
        raise NotImplementedError
