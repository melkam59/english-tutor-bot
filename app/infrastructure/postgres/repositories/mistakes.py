from dataclasses import dataclass

from app.application.ports.repositories.mistakes import MistakesGateway
from app.domain.user_mistake import UserMistake
from app.infrastructure.postgres.repository_helper import SqlRepositoryHelper
from app.infrastructure.postgres.uow import UoW


@dataclass
class MistakesRepository(MistakesGateway):
    # TODO(M3): implement every method of MistakesGateway
    _uow: UoW
    _helper: SqlRepositoryHelper[UserMistake]
