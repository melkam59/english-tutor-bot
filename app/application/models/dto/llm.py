from app.application.models.base import PydanticModel
from app.domain.enums.message_role import MessageRole
from app.domain.enums.mistake_category import MistakeCategory


class LLMMessage(PydanticModel):
    role: MessageRole
    text: str


class LLMUsage(PydanticModel):
    input_tokens: int = 0
    output_tokens: int = 0


class LLMResponse(PydanticModel):
    text: str
    usage: LLMUsage
    latency_ms: int = 0


class Correction(PydanticModel):
    original_text: str
    corrected_text: str
    # Written in the user's native language
    explanation: str
    category: MistakeCategory


class TutorReply(PydanticModel):
    """Structured tutor output the LLM is asked to produce for every user message."""

    corrected_text: str | None = None
    corrections: list[Correction] = []
    better_phrases: list[str] = []
    reply: str
    usage: LLMUsage = LLMUsage()
