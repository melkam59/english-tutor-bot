from dataclasses import dataclass
from typing import Optional

from app.application.interactors.base import BaseInteractor
from app.application.models.dto.llm import TutorReply
from app.application.ports.llm.gateway import LLMGateway
from app.application.ports.repositories.conversations import ConversationsGateway
from app.application.ports.repositories.messages import MessagesGateway
from app.application.ports.repositories.mistakes import MistakesGateway
from app.application.services.access import AccessPolicy
from app.application.services.context import ConversationContextService
from app.application.services.prompts import PromptBuilder
from app.domain.conversation import Conversation
from app.domain.enums.practice_mode import PracticeMode, RolePlayScenario
from app.domain.user import User


@dataclass(frozen=True)
class TutorConversationInteractor(BaseInteractor):
    """Core AI conversation mode: correct, explain, continue the dialogue."""

    user: User
    llm: LLMGateway
    prompts: PromptBuilder
    context: ConversationContextService
    access: AccessPolicy
    conversations_gateway: ConversationsGateway
    messages_gateway: MessagesGateway
    mistakes_gateway: MistakesGateway

    async def start(
        self,
        mode: PracticeMode,
        scenario: Optional[RolePlayScenario] = None,
    ) -> Conversation:
        # TODO(M2): access.can_use_mode -> PremiumRequiredError, deactivate previous, create new
        raise NotImplementedError

    async def reply(self, text: str) -> TutorReply:
        # TODO(M2):
        #  1. get or create the active conversation
        #  2. build system prompt (profile + mode + recent mistakes + summary)
        #  3. context.build_context + user message -> llm.complete(json_schema=...)
        #  4. parse TutorReply, raise LLMInvalidResponseError on a broken payload
        #  5. store both messages and corrections, context.summarize_if_needed
        raise NotImplementedError
