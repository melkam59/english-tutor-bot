import pytest

pytestmark = pytest.mark.skip(reason="scaffold: implement together with M2")


# Use tests.mocks.llm.FakeLLMGateway, external APIs must never be called.


def test_reply_contains_correction_and_follow_up() -> None: ...


def test_only_limited_context_is_sent_to_llm() -> None: ...


def test_conversation_is_summarized_after_threshold() -> None: ...


def test_invalid_llm_payload_raises_invalid_response_error() -> None: ...
