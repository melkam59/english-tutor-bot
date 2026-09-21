from dataclasses import dataclass

from app.application.ports.repositories.usage import UsageGateway
from app.domain.usage_record import UsageRecord
from app.infrastructure.postgres.repository_helper import SqlRepositoryHelper
from app.infrastructure.postgres.uow import UoW


@dataclass
class UsageRepository(UsageGateway):
    # TODO(M4): implement every method of UsageGateway
    _uow: UoW
    _helper: SqlRepositoryHelper[UsageRecord]
