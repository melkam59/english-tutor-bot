from dataclasses import dataclass
from typing import Optional

from pydantic import ValidationError

from app.application.errors.llm import LLMInvalidResponseError
from app.application.interactors.base import BaseInteractor
from app.application.models.config import AppConfig
from app.application.models.dto.llm import LLMMessage, LLMResponse, TutorReply
from app.application.ports.llm.gateway import LLMGateway
from app.application.ports.repositories.conversations import ConversationsGateway
from app.application.ports.repositories.messages import MessagesGateway
from app.application.ports.repositories.mistakes import MistakesGateway
from app.application.services.access import AccessPolicy
from app.application.services.context import ConversationContextService
from app.application.services.prompts import PromptBuilder
from app.domain.conversation import Conversation
from app.domain.enums.message_role import MessageRole
from app.domain.enums.practice_mode import PracticeMode, RolePlayScenario
from app.domain.user import User


@dataclass(frozen=True)
class TutorConversationInteractor(BaseInteractor):
    """Core AI conversation mode: correct, explain, continue the dialogue."""

    user: User
    config: AppConfig
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
        conversation = await self.conversations_gateway.get_active(user_id=self.user.id)
        if conversation is None:
            conversation = await self.conversations_gateway.create(
                user_id=self.user.id,
                mode=PracticeMode.GENERAL,
            )
        recent_mistakes = await self.mistakes_gateway.get_recent(
            user_id=self.user.id,
            limit=self.config.llm.recent_mistakes_in_prompt,
        )
        history = await self.context.build_context(conversation)
        response: LLMResponse = await self.llm.complete(
            system_prompt=self.prompts.tutor_system_prompt(
                user=self.user,
                conversation=conversation,
                recent_mistakes=recent_mistakes,
            ),
            messages=[*history, LLMMessage(role=MessageRole.USER, text=text)],
            json_schema=self.prompts.tutor_reply_schema(),
        )
        reply = self._parse(response)
        await self.messages_gateway.add(
            conversation_id=conversation.id,
            role=MessageRole.USER,
            text=text,
            token_usage=response.usage.input_tokens,
        )
        await self.messages_gateway.add(
            conversation_id=conversation.id,
            role=MessageRole.ASSISTANT,
            text=reply.reply,
            token_usage=response.usage.output_tokens,
        )
        if reply.corrections:
            await self.mistakes_gateway.add_many(
                user_id=self.user.id,
                corrections=reply.corrections,
            )
        return reply

    @staticmethod
    def _parse(response: LLMResponse) -> TutorReply:
        payload: str = response.text.strip().removeprefix("```json").removesuffix("```").strip()
        try:
            reply = TutorReply.model_validate_json(payload)
        except ValidationError as error:
            raise LLMInvalidResponseError() from error
        reply.usage = response.usage
        return reply
