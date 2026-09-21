from dataclasses import dataclass
from decimal import Decimal

from app.application.ports.repositories.usage import UsageGateway
from app.domain.enums.request_type import RequestType
from app.domain.usage_record import UsageRecord
from app.infrastructure.postgres.repository_helper import SqlRepositoryHelper
from app.infrastructure.postgres.uow import UoW


@dataclass
class UsageRepository(UsageGateway):
    # TODO(M4): count_since / sum_tokens_since / sum_cost_since for admin statistics
    _uow: UoW
    _helper: SqlRepositoryHelper[UsageRecord]

    async def add(
        self,
        user_id: int,
        request_type: RequestType,
        input_tokens: int,
        output_tokens: int,
        estimated_cost: Decimal,
    ) -> UsageRecord:
        record = UsageRecord(
            user_id=user_id,
            request_type=request_type,
            input_tokens=input_tokens,
            output_tokens=output_tokens,
            estimated_cost=estimated_cost,
        )
        await self._uow.commit(record)
        return record
