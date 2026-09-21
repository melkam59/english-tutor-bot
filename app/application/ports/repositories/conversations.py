from typing import Optional, Protocol

from app.domain.conversation import Conversation
from app.domain.enums.practice_mode import PracticeMode, RolePlayScenario


class ConversationsGateway(Protocol):
    async def get_active(self, user_id: int) -> Optional[Conversation]: ...

    async def create(
        self,
        user_id: int,
        mode: PracticeMode,
        scenario: Optional[RolePlayScenario] = None,
    ) -> Conversation: ...

    async def save(self, conversation: Conversation) -> None: ...

    async def deactivate_all(self, user_id: int) -> None: ...

    async def count(self, user_id: int) -> int: ...
