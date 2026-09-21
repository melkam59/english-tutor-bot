from dataclasses import dataclass
from datetime import timedelta

from app.application.interactors.base import BaseInteractor
from app.application.models.dto.progress import ProgressSummary
from app.application.ports.repositories.conversations import ConversationsGateway
from app.application.ports.repositories.lessons import LessonsGateway
from app.application.ports.repositories.mistakes import MistakesGateway
from app.application.ports.repositories.users import UsersGateway
from app.application.ports.repositories.vocabulary import VocabularyGateway
from app.domain.user import User
from app.utils.time import datetime_now


@dataclass(frozen=True)
class ProgressInteractor(BaseInteractor):
    user: User
    users_gateway: UsersGateway
    lessons_gateway: LessonsGateway
    conversations_gateway: ConversationsGateway
    vocabulary_gateway: VocabularyGateway
    mistakes_gateway: MistakesGateway

    async def get_summary(self) -> ProgressSummary:
        user_id: int = self.user.id
        return ProgressSummary(
            level=self.user.english_level,
            completed_lessons=await self.lessons_gateway.count_completed(user_id=user_id),
            practice_sessions=await self.conversations_gateway.count(user_id=user_id),
            learned_words=await self.vocabulary_gateway.count(user_id=user_id),
            common_mistakes=await self.mistakes_gateway.get_top_categories(
                user_id=user_id,
                limit=3,
            ),
            total_study_seconds=self.user.total_study_seconds,
            current_streak=self.user.current_streak,
        )

    async def track_activity(self, study_seconds: int = 0) -> None:
        now = datetime_now()
        today = now.date()
        if self.user.last_study_date != today:
            studied_yesterday: bool = self.user.last_study_date == today - timedelta(days=1)
            self.user.current_streak = self.user.current_streak + 1 if studied_yesterday else 1
            self.user.last_study_date = today
        self.user.last_activity_at = now
        self.user.total_study_seconds += study_seconds
        await self.users_gateway.save(self.user)
