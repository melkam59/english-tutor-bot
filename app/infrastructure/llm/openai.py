import logging
import time
from dataclasses import dataclass, field
from typing import Any, Final, Optional

import httpx2
from openai import APIError, APITimeoutError, AsyncOpenAI, RateLimitError

from app.application.errors.llm import LLMError, LLMRateLimitError, LLMTimeoutError
from app.application.models.config.env import LLMConfig, LLMProviderType
from app.application.models.dto.llm import LLMMessage, LLMResponse, LLMUsage
from app.application.ports.llm.gateway import LLMGateway
from app.utils.custom_types import DictStrAny

logger: Final[logging.Logger] = logging.getLogger(name=__name__)

_DEFAULT_BASE_URLS: Final[dict[LLMProviderType, str]] = {
    LLMProviderType.DEEPSEEK: "https://api.deepseek.com",
}


@dataclass
class OpenAIGateway(LLMGateway):
    """OpenAI and every OpenAI-compatible API (DeepSeek, OpenRouter, ...)."""

    config: LLMConfig
    http_client: Optional[httpx2.AsyncClient] = None
    _client: AsyncOpenAI = field(init=False, repr=False)

    def __post_init__(self) -> None:
        self._client = AsyncOpenAI(
            api_key=self.config.api_key.get_secret_value(),
            base_url=self.config.base_url or _DEFAULT_BASE_URLS.get(self.config.provider),
            timeout=self.config.request_timeout,
            max_retries=self.config.max_retries,
            http_client=self.http_client,
        )

    async def complete(
        self,
        system_prompt: str,
        messages: list[LLMMessage],
        model: Optional[str] = None,
        max_output_tokens: Optional[int] = None,
        json_schema: Optional[DictStrAny] = None,
    ) -> LLMResponse:
        payload: list[Any] = [
            {"role": "system", "content": system_prompt},
            *({"role": message.role.value, "content": message.text} for message in messages),
        ]
        extra: dict[str, Any] = {}
        if json_schema is not None:
            # JSON mode is the common denominator, the exact shape is described in the prompt
            extra["response_format"] = {"type": "json_object"}

        started_at: float = time.monotonic()
        try:
            completion = await self._client.chat.completions.create(
                model=model or self.config.model,
                messages=payload,
                max_tokens=max_output_tokens or self.config.max_output_tokens,
                temperature=self.config.temperature,
                **extra,
            )
        except APITimeoutError as error:
            raise LLMTimeoutError() from error
        except RateLimitError as error:
            raise LLMRateLimitError() from error
        except APIError as error:
            logger.error("LLM request failed: %s", type(error).__name__)
            raise LLMError() from error

        latency_ms: int = int((time.monotonic() - started_at) * 1000)
        usage = LLMUsage(
            input_tokens=completion.usage.prompt_tokens if completion.usage else 0,
            output_tokens=completion.usage.completion_tokens if completion.usage else 0,
        )
        logger.info(
            "LLM request: model=%s latency_ms=%d input_tokens=%d output_tokens=%d",
            completion.model,
            latency_ms,
            usage.input_tokens,
            usage.output_tokens,
        )
        return LLMResponse(
            text=completion.choices[0].message.content or "",
            usage=usage,
            latency_ms=latency_ms,
        )
