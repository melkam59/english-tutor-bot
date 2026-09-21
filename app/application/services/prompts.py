from dataclasses import dataclass
from functools import cache
from typing import Optional

from app.application.models.dto.llm import TutorReply
from app.const import PROMPTS_SOURCE_DIR
from app.domain.conversation import Conversation
from app.domain.enums.english_level import EnglishLevel
from app.domain.user import User
from app.domain.user_mistake import UserMistake
from app.domain.vocabulary_item import VocabularyItem
from app.utils.custom_types import DictStrAny


@cache
def _load_template(name: str) -> str:
    return (PROMPTS_SOURCE_DIR / f"{name}.md").read_text(encoding="utf-8")


def _render(template: str, **values: str) -> str:
    # Not str.format: the templates contain literal JSON braces
    for key, value in values.items():
        template = template.replace("{" + key + "}", value)
    return template


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
        mode: str = conversation.mode.value
        if conversation.scenario is not None:
            mode += f" ({conversation.scenario.value})"
        mistakes: str = "\n".join(
            f"- [{mistake.category.value}] {mistake.original_text} -> {mistake.corrected_text}"
            for mistake in recent_mistakes
        )
        return _render(
            _load_template("tutor_system"),
            level=user.english_level.value if user.english_level else "unknown",
            native_language=user.native_language or "en",
            goal=user.learning_goal.value if user.learning_goal else "general",
            mode=mode,
            recent_mistakes=mistakes or "none yet",
            summary=conversation.summary or "this is the beginning of the conversation",
        )

    def tutor_reply_schema(self) -> DictStrAny:
        return TutorReply.model_json_schema()

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
