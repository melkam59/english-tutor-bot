from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from app.application.models.dto.llm import Correction
from app.application.ports.limits.rate_limiter import UsageCounter
from app.application.ports.repositories.conversations import ConversationsGateway
from app.application.ports.repositories.lessons import LessonsGateway
from app.application.ports.repositories.messages import MessagesGateway
from app.application.ports.repositories.mistakes import MistakesGateway
from app.application.ports.repositories.usage import UsageGateway
from app.application.ports.repositories.users import UsersGateway
from app.application.ports.repositories.vocabulary import VocabularyGateway
from app.domain.conversation import Conversation
from app.domain.enums.message_role import MessageRole
from app.domain.enums.mistake_category import MistakeCategory
from app.domain.enums.practice_mode import PracticeMode, RolePlayScenario
from app.domain.enums.request_type import RequestType
from app.domain.enums.subscription import SubscriptionType
from app.domain.message import Message
from app.domain.usage_record import UsageRecord
from app.domain.user import User
from app.domain.user_mistake import UserMistake


def make_user(**kwargs: object) -> User:
    defaults: dict[str, object] = {
        "id": 1,
        "name": "Test",
        "language": "en",
        "subscription_type": SubscriptionType.FREE,
        "current_streak": 0,
        "total_study_seconds": 0,
    }
    return User(**(defaults | kwargs))


@dataclass
class FakeUsersGateway(UsersGateway):
    users: dict[int, User] = field(default_factory=dict)

    async def get(self, user_id: int) -> Optional[User]:
        return self.users.get(user_id)

    async def save(self, user: User) -> None:
        self.users[user.id] = user


@dataclass
class FakeConversationsGateway(ConversationsGateway):
    items: list[Conversation] = field(default_factory=list)

    async def get_active(self, user_id: int) -> Optional[Conversation]:
        for item in reversed(self.items):
            if item.user_id == user_id and item.is_active:
                return item
        return None

    async def create(
        self,
        user_id: int,
        mode: PracticeMode,
        scenario: Optional[RolePlayScenario] = None,
    ) -> Conversation:
        item = Conversation(
            id=len(self.items) + 1,
            user_id=user_id,
            mode=mode,
            scenario=scenario,
            is_active=True,
        )
        self.items.append(item)
        return item

    async def save(self, conversation: Conversation) -> None:
        pass

    async def deactivate_all(self, user_id: int) -> None:
        for item in self.items:
            if item.user_id == user_id:
                item.is_active = False

    async def count(self, user_id: int) -> int:
        return len([item for item in self.items if item.user_id == user_id])


@dataclass
class FakeMessagesGateway(MessagesGateway):
    items: list[Message] = field(default_factory=list)

    async def add(
        self,
        conversation_id: int,
        role: MessageRole,
        text: str,
        token_usage: int = 0,
    ) -> Message:
        item = Message(
            id=len(self.items) + 1,
            conversation_id=conversation_id,
            role=role,
            text=text,
            token_usage=token_usage,
        )
        self.items.append(item)
        return item

    async def get_recent(self, conversation_id: int, limit: int) -> list[Message]:
        items = [item for item in self.items if item.conversation_id == conversation_id]
        return items[-limit:]

    async def count(self, conversation_id: int) -> int:
        return len([item for item in self.items if item.conversation_id == conversation_id])


@dataclass
class FakeMistakesGateway(MistakesGateway):
    items: list[UserMistake] = field(default_factory=list)

    async def add_many(self, user_id: int, corrections: list[Correction]) -> None:
        for correction in corrections:
            self.items.append(UserMistake(user_id=user_id, **correction.model_dump()))

    async def get_recent(self, user_id: int, limit: int) -> list[UserMistake]:
        return [item for item in self.items if item.user_id == user_id][-limit:]

    async def get_top_categories(
        self,
        user_id: int,
        limit: int,
    ) -> list[tuple[MistakeCategory, int]]:
        counts: dict[MistakeCategory, int] = {}
        for item in self.items:
            if item.user_id == user_id:
                counts[item.category] = counts.get(item.category, 0) + 1
        return sorted(counts.items(), key=lambda pair: -pair[1])[:limit]


@dataclass
class FakeUsageCounter(UsageCounter):
    messages: dict[int, int] = field(default_factory=dict)
    voice: dict[int, int] = field(default_factory=dict)

    async def get_messages(self, user_id: int) -> int:
        return self.messages.get(user_id, 0)

    async def increment_messages(self, user_id: int) -> int:
        self.messages[user_id] = self.messages.get(user_id, 0) + 1
        return self.messages[user_id]

    async def get_voice_messages(self, user_id: int) -> int:
        return self.voice.get(user_id, 0)

    async def increment_voice_messages(self, user_id: int) -> int:
        self.voice[user_id] = self.voice.get(user_id, 0) + 1
        return self.voice[user_id]


@dataclass
class FakeUsageGateway(UsageGateway):
    items: list[UsageRecord] = field(default_factory=list)

    async def add(
        self,
        user_id: int,
        request_type: RequestType,
        input_tokens: int,
        output_tokens: int,
        estimated_cost: Decimal,
    ) -> UsageRecord:
        item = UsageRecord(
            user_id=user_id,
            request_type=request_type,
            input_tokens=input_tokens,
            output_tokens=output_tokens,
            estimated_cost=estimated_cost,
        )
        self.items.append(item)
        return item


@dataclass
class FakeLessonsGateway(LessonsGateway):
    completed: int = 0

    async def count_completed(self, user_id: int) -> int:
        return self.completed


@dataclass
class FakeVocabularyGateway(VocabularyGateway):
    total: int = 0

    async def count(self, user_id: int) -> int:
        return self.total
