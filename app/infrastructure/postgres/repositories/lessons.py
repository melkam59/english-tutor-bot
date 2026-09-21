from dataclasses import dataclass

from app.application.ports.repositories.lessons import LessonsGateway
from app.domain.lesson import Lesson
from app.infrastructure.postgres.repository_helper import SqlRepositoryHelper
from app.infrastructure.postgres.uow import UoW


@dataclass
class LessonsRepository(LessonsGateway):
    # TODO(M3): implement every method of LessonsGateway
    _uow: UoW
    _helper: SqlRepositoryHelper[Lesson]
