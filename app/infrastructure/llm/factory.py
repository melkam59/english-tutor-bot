from typing import Final

from app.application.models.config.env import LLMConfig, LLMProviderType
from app.application.ports.llm.gateway import LLMGateway

from .anthropic import AnthropicGateway
from .gemini import GeminiGateway
from .openai import OpenAIGateway

_PROVIDERS: Final[dict[LLMProviderType, type[LLMGateway]]] = {
    # DeepSeek speaks the OpenAI protocol
    LLMProviderType.DEEPSEEK: OpenAIGateway,
    LLMProviderType.OPENAI: OpenAIGateway,
    LLMProviderType.ANTHROPIC: AnthropicGateway,
    LLMProviderType.GEMINI: GeminiGateway,
}


def create_llm_gateway(config: LLMConfig) -> LLMGateway:
    """To add a provider: implement ``LLMGateway`` and register it in ``_PROVIDERS``."""
    return _PROVIDERS[config.provider](config=config)  # type: ignore[call-arg]
