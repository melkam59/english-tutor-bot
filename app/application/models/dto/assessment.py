from app.application.models.base import PydanticModel
from app.domain.enums.english_level import EnglishLevel


class AssessmentQuestion(PydanticModel):
    id: int
    level: EnglishLevel
    text: str
    # Empty for short written answers
    options: list[str] = []
    correct_option: int | None = None


class AssessmentResult(PydanticModel):
    level: EnglishLevel
    correct_answers: int
    total_questions: int
