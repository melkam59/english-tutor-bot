from dataclasses import dataclass

from app.application.interactors.base import BaseInteractor
from app.application.models.dto.assessment import AssessmentQuestion, AssessmentResult
from app.application.models.state.assessment import AssessmentState
from app.application.ports.llm.gateway import LLMGateway
from app.application.ports.repositories.users import UsersGateway
from app.application.services.assessment_bank import AssessmentBank
from app.application.services.prompts import PromptBuilder
from app.domain.user import User


@dataclass(frozen=True)
class LevelAssessmentInteractor(BaseInteractor):
    user: User
    users_gateway: UsersGateway
    bank: AssessmentBank
    llm: LLMGateway
    prompts: PromptBuilder

    def next_question(self, state: AssessmentState) -> AssessmentQuestion | None:
        # TODO(M3): None when the assessment is over
        raise NotImplementedError

    async def finish(self, state: AssessmentState) -> AssessmentResult:
        # TODO(M3): bank.estimate_level + optional LLM grading of the written answer,
        #  then store the result in user.english_level
        raise NotImplementedError
