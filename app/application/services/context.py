from dataclasses import dataclass

from app.application.models.config import AppConfig
from app.application.models.dto.llm import LLMMessage
from app.application.ports.llm.gateway import LLMGateway
from app.application.ports.repositories.conversations import ConversationsGateway
from app.application.ports.repositories.messages import MessagesGateway
from app.application.services.prompts import PromptBuilder
from app.domain.conversation import Conversation


@dataclass(frozen=True)
class ConversationContextService:
    """
    Limited-context strategy: the LLM only ever receives the rolling
    ``Conversation.summary`` plus the last ``LLM_CONTEXT_MESSAGES`` messages.
    """

    config: AppConfig
    llm: LLMGateway
    prompts: PromptBuilder
    conversations_gateway: ConversationsGateway
    messages_gateway: MessagesGateway

    async def build_context(self, conversation: Conversation) -> list[LLMMessage]:
        messages = await self.messages_gateway.get_recent(
            conversation_id=conversation.id,
            limit=self.config.llm.context_messages,
        )
        return [LLMMessage(role=message.role, text=message.text) for message in messages]

    async def summarize_if_needed(self, conversation: Conversation) -> None:
        # TODO(M2): once count > config.llm.summarize_after_messages fold the older
        #  messages into conversation.summary using config.llm.summary_model
        raise NotImplementedError
