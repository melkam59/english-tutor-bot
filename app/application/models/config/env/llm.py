from enum import StrEnum, auto
from typing import Optional

from pydantic import SecretStr

from .base import EnvSettings


# noinspection PyEnum
class LLMProviderType(StrEnum):
    DEEPSEEK = auto()
    OPENAI = auto()
    ANTHROPIC = auto()
    GEMINI = auto()


class LLMConfig(EnvSettings, env_prefix="LLM_"):
    provider: LLMProviderType
    api_key: SecretStr
    # Override for OpenAI-compatible APIs, DeepSeek gets its default automatically
    base_url: Optional[str] = None
    model: str
    # Cheaper model used for conversation summarization
    summary_model: str
    request_timeout: float = 30.0
    max_retries: int = 2
    max_output_tokens: int = 600
    temperature: float = 0.7
    # Limited-context strategy: only the last N messages + rolling summary are sent
    context_messages: int = 12
    summarize_after_messages: int = 20
    recent_mistakes_in_prompt: int = 5
    # USD per 1M tokens, used for approximate cost tracking
    input_price_per_million: float = 0.0
    output_price_per_million: float = 0.0
