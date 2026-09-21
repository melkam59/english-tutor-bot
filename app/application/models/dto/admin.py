from decimal import Decimal

from app.application.models.base import PydanticModel


class AdminStats(PydanticModel):
    total_users: int
    active_users: int
    new_users: int
    llm_requests: int
    input_tokens: int
    output_tokens: int
    estimated_cost: Decimal


class BroadcastResult(PydanticModel):
    sent: int
    failed: int
