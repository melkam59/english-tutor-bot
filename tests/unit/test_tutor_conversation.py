import json
from dataclasses import dataclass

import pytest

from app.application.errors.llm import LLMInvalidResponseError
from app.application.interactors.tutor.conversation import TutorConversationInteractor
from app.application.services.access import AccessPolicy
from app.application.services.context import ConversationContextService
from app.application.services.prompts import PromptBuilder
from app.domain.enums.english_level import EnglishLevel
from app.domain.enums.learning_goal import LearningGoal
from app.domain.enums.mistake_category import MistakeCategory
from app.providers.infrastructure.app import create_app_config
from tests.mocks.gateways import (
    FakeConversationsGateway,
    FakeMessagesGateway,
    FakeMistakesGateway,
    make_user,
)
from tests.mocks.llm import FakeLLMGateway

CINEMA_REPLY: str = json.dumps(
    {
        "corrected_text": "Yesterday I went to the cinema with my friend.",
        "corrections": [
            {
                "original_text": "I go to cinema",
                "corrected_text": "I went to the cinema",
                "explanation": "Używamy „went”, bo czynność miała miejsce w przeszłości.",
                "category": "verb_tense",
            }
        ],
        "better_phrases": [],
        "reply": "What movie did you watch?",
    }
)
CLEAN_REPLY: str = json.dumps({"corrections": [], "reply": "Nice! Tell me more."})


@dataclass
class Tutor:
    interactor: TutorConversationInteractor
    llm: FakeLLMGateway
    messages: FakeMessagesGateway
    mistakes: FakeMistakesGateway


def make_tutor(responses: list[str]) -> Tutor:
    llm = FakeLLMGateway(responses=responses)
    conversations = FakeConversationsGateway()
    messages = FakeMessagesGateway()
    mistakes = FakeMistakesGateway()
    prompts = PromptBuilder()
    config = create_app_config()
    interactor = TutorConversationInteractor(
        user=make_user(
            native_language="pl",
            english_level=EnglishLevel.A2,
            learning_goal=LearningGoal.TRAVEL,
        ),
        config=config,
        llm=llm,
        prompts=prompts,
        context=ConversationContextService(
            config=config,
            llm=llm,
            prompts=prompts,
            conversations_gateway=conversations,
            messages_gateway=messages,
        ),
        access=AccessPolicy(),
        conversations_gateway=conversations,
        messages_gateway=messages,
        mistakes_gateway=mistakes,
    )
    return Tutor(interactor=interactor, llm=llm, messages=messages, mistakes=mistakes)


async def test_reply_contains_correction_and_follow_up() -> None:
    tutor = make_tutor([CINEMA_REPLY])

    reply = await tutor.interactor.reply("Yesterday I go to cinema with my friend.")

    assert reply.corrected_text == "Yesterday I went to the cinema with my friend."
    assert reply.corrections[0].category is MistakeCategory.VERB_TENSE
    assert reply.reply == "What movie did you watch?"


async def test_previous_exchange_is_sent_as_context() -> None:
    tutor = make_tutor([CINEMA_REPLY, CLEAN_REPLY])

    await tutor.interactor.reply("Yesterday I go to cinema with my friend.")
    await tutor.interactor.reply("We watched Dune.")

    _, sent = tutor.llm.calls[1]
    assert [message.text for message in sent] == [
        "Yesterday I go to cinema with my friend.",
        "What movie did you watch?",
        "We watched Dune.",
    ]


async def test_corrections_are_remembered_for_next_prompts() -> None:
    tutor = make_tutor([CINEMA_REPLY, CLEAN_REPLY])

    await tutor.interactor.reply("Yesterday I go to cinema with my friend.")
    await tutor.interactor.reply("We watched Dune.")

    assert tutor.mistakes.items[0].category is MistakeCategory.VERB_TENSE
    system_prompt, _ = tutor.llm.calls[1]
    assert "I go to cinema -> I went to the cinema" in system_prompt


async def test_only_limited_context_is_sent_to_llm() -> None:
    limit = create_app_config().llm.context_messages
    tutor = make_tutor([CLEAN_REPLY] * (limit + 1))

    for index in range(limit + 1):
        await tutor.interactor.reply(f"Message number {index}")

    _, sent = tutor.llm.calls[-1]
    assert len(sent) == limit + 1  # the context window plus the new message
    assert "Message number 0" not in [message.text for message in sent]


async def test_invalid_llm_payload_raises_invalid_response_error() -> None:
    tutor = make_tutor(["Sorry, I cannot answer in JSON today"])

    with pytest.raises(LLMInvalidResponseError):
        await tutor.interactor.reply("Hello")

    assert tutor.messages.items == []
