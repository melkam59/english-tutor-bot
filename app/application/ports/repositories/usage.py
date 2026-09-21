from datetime import datetime
from decimal import Decimal
from typing import Protocol

from app.domain.enums.request_type import RequestType
from app.domain.usage_record import UsageRecord


class UsageGateway(Protocol):
    async def add(
        self,
        user_id: int,
        request_type: RequestType,
        input_tokens: int,
        output_tokens: int,
        estimated_cost: Decimal,
    ) -> UsageRecord: ...

    async def count_since(self, since: datetime) -> int: ...

    async def sum_tokens_since(self, since: datetime) -> tuple[int, int]: ...

    async def sum_cost_since(self, since: datetime) -> Decimal: ...
