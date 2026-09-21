import json

import httpx2
import pytest

from app.application.errors.llm import LLMRateLimitError
from app.application.models.config.env import LLMConfig, LLMProviderType
from app.application.models.dto.llm import LLMMessage
from app.domain.enums.message_role import MessageRole
from app.infrastructure.llm.factory import create_llm_gateway
from app.infrastructure.llm.openai import OpenAIGateway


def make_gateway(handler: httpx2.MockTransport) -> OpenAIGateway:
    config = LLMConfig(provider=LLMProviderType.DEEPSEEK, model="deepseek-chat", max_retries=0)
    return OpenAIGateway(config=config, http_client=httpx2.AsyncClient(transport=handler))


async def test_deepseek_request_and_usage_mapping() -> None:
    requests: list[httpx2.Request] = []

    def handler(request: httpx2.Request) -> httpx2.Response:
        requests.append(request)
        return httpx2.Response(
            200,
            json={
                "id": "1",
                "object": "chat.completion",
                "created": 0,
                "model": "deepseek-chat",
                "choices": [
                    {
                        "index": 0,
                        "finish_reason": "stop",
                        "message": {"role": "assistant", "content": '{"reply": "Hi!"}'},
                    }
                ],
                "usage": {"prompt_tokens": 11, "completion_tokens": 7, "total_tokens": 18},
            },
        )

    gateway = make_gateway(httpx2.MockTransport(handler))
    response = await gateway.complete(
        system_prompt="You are a tutor",
        messages=[LLMMessage(role=MessageRole.USER, text="Hello")],
        json_schema={"type": "object"},
    )

    assert response.text == '{"reply": "Hi!"}'
    assert (response.usage.input_tokens, response.usage.output_tokens) == (11, 7)
    body = json.loads(requests[0].content)
    assert requests[0].url.host == "api.deepseek.com"
    assert body["model"] == "deepseek-chat"
    assert body["messages"][0] == {"role": "system", "content": "You are a tutor"}
    assert body["response_format"] == {"type": "json_object"}


async def test_rate_limit_is_mapped_to_application_error() -> None:
    gateway = make_gateway(
        httpx2.MockTransport(lambda _: httpx2.Response(429, json={"error": {"message": "slow"}}))
    )

    with pytest.raises(LLMRateLimitError):
        await gateway.complete(system_prompt="", messages=[])


def test_factory_builds_deepseek_gateway() -> None:
    config = LLMConfig(provider=LLMProviderType.DEEPSEEK)

    assert isinstance(create_llm_gateway(config), OpenAIGateway)
