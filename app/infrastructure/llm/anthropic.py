from dataclasses import dataclass
from typing import Optional

from app.application.models.config.env import LLMConfig
from app.application.models.dto.llm import LLMMessage, LLMResponse
from app.application.ports.llm.gateway import LLMGateway
from app.utils.custom_types import DictStrAny


@dataclass
class AnthropicGateway(LLMGateway):
    config: LLMConfig

    async def complete(
        self,
        system_prompt: str,
        messages: list[LLMMessage],
        model: Optional[str] = None,
        max_output_tokens: Optional[int] = None,
        json_schema: Optional[DictStrAny] = None,
    ) -> LLMResponse:
        # TODO(M2): call the Anthropic SDK (AsyncAnthropic),
        #  honour config.request_timeout / config.max_retries,
        #  map timeouts -> LLMTimeoutError, 429 -> LLMRateLimitError, fill LLMUsage,
        #  log latency and token usage (never the API key or full user text)
        raise NotImplementedError
