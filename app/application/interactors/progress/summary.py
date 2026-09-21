from dataclasses import dataclass

from app.application.interactors.base import BaseInteractor
from app.application.models.dto.progress import ProgressSummary
from app.application.ports.repositories.conversations import ConversationsGateway
from app.application.ports.repositories.lessons import LessonsGateway
from app.application.ports.repositories.mistakes import MistakesGateway
from app.application.ports.repositories.users import UsersGateway
from app.application.ports.repositories.vocabulary import VocabularyGateway
from app.domain.user import User


@dataclass(frozen=True)
class ProgressInteractor(BaseInteractor):
    user: User
    users_gateway: UsersGateway
    lessons_gateway: LessonsGateway
    conversations_gateway: ConversationsGateway
    vocabulary_gateway: VocabularyGateway
    mistakes_gateway: MistakesGateway

    async def get_summary(self) -> ProgressSummary:
        # TODO(M3)
        raise NotImplementedError

    async def track_activity(self, study_seconds: int = 0) -> None:
        # TODO(M3): last_activity_at, total_study_seconds, streak based on last_study_date
        raise NotImplementedError
