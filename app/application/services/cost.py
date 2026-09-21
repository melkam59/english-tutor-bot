from dataclasses import dataclass
from decimal import Decimal

from app.application.models.config import AppConfig
from app.application.models.dto.llm import LLMUsage


@dataclass(frozen=True)
class CostEstimator:
    config: AppConfig

    def llm_cost(self, usage: LLMUsage) -> Decimal:
        llm = self.config.llm
        return (
            Decimal(usage.input_tokens) * Decimal(str(llm.input_price_per_million))
            + Decimal(usage.output_tokens) * Decimal(str(llm.output_price_per_million))
        ) / Decimal(1_000_000)

    def stt_cost(self, duration_seconds: int) -> Decimal:
        # TODO(M4): duration / 60 * config.speech.stt_price_per_minute
        raise NotImplementedError
