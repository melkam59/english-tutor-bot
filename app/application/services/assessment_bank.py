from dataclasses import dataclass

from app.application.models.config import Assets
from app.application.models.dto.assessment import AssessmentQuestion, AssessmentResult


@dataclass(frozen=True)
class AssessmentBank:
    """Static question bank loaded from ``assets/assessment.yml``."""

    assets: Assets

    def get_questions(self) -> list[AssessmentQuestion]:
        return self.assets.assessment

    def estimate_level(self, answers: dict[int, int | str]) -> AssessmentResult:
        # TODO(M3): highest level where the user answered >= ~60% correctly
        raise NotImplementedError
