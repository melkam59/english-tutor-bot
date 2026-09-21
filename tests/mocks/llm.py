from dataclasses import dataclass, field
from typing import Optional

from app.application.models.dto.llm import LLMMessage, LLMResponse, LLMUsage
from app.application.ports.llm.gateway import LLMGateway
from app.utils.custom_types import DictStrAny


@dataclass
class FakeLLMGateway(LLMGateway):
    """External APIs are never called in tests: queue canned responses instead."""

    responses: list[str] = field(default_factory=list)
    calls: list[tuple[str, list[LLMMessage]]] = field(default_factory=list)

    async def complete(
        self,
        system_prompt: str,
        messages: list[LLMMessage],
        model: Optional[str] = None,
        max_output_tokens: Optional[int] = None,
        json_schema: Optional[DictStrAny] = None,
    ) -> LLMResponse:
        self.calls.append((system_prompt, messages))
        return LLMResponse(
            text=self.responses.pop(0),
            usage=LLMUsage(input_tokens=10, output_tokens=20),
        )
