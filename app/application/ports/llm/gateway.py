from typing import Optional, Protocol

from app.application.models.dto.llm import LLMMessage, LLMResponse
from app.utils.custom_types import DictStrAny


class LLMGateway(Protocol):
    """
    Provider-agnostic LLM port. Implementations live in ``app/infrastructure/llm``
    and must translate provider errors into ``app.application.errors.llm`` errors.
    """

    async def complete(
        self,
        system_prompt: str,
        messages: list[LLMMessage],
        model: Optional[str] = None,
        max_output_tokens: Optional[int] = None,
        json_schema: Optional[DictStrAny] = None,
    ) -> LLMResponse: ...
