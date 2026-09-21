from dataclasses import dataclass
from decimal import Decimal

from app.application.models.config import AppConfig
from app.application.models.dto.llm import LLMUsage


@dataclass(frozen=True)
class CostEstimator:
    config: AppConfig

    def llm_cost(self, usage: LLMUsage) -> Decimal:
        # TODO(M4): tokens / 1_000_000 * config.llm.{input,output}_price_per_million
        raise NotImplementedError

    def stt_cost(self, duration_seconds: int) -> Decimal:
        # TODO(M4): duration / 60 * config.speech.stt_price_per_minute
        raise NotImplementedError
