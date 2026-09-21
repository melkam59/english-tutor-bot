from app.application.models.base import PydanticModel
from app.domain.enums.english_level import EnglishLevel
from app.domain.enums.mistake_category import MistakeCategory


class ProgressSummary(PydanticModel):
    level: EnglishLevel | None
    completed_lessons: int
    practice_sessions: int
    learned_words: int
    common_mistakes: list[tuple[MistakeCategory, int]]
    total_study_seconds: int
    current_streak: int
