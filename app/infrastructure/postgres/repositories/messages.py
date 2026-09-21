from dataclasses import dataclass

from app.application.ports.repositories.messages import MessagesGateway
from app.domain.message import Message
from app.infrastructure.postgres.repository_helper import SqlRepositoryHelper
from app.infrastructure.postgres.uow import UoW


@dataclass
class MessagesRepository(MessagesGateway):
    # TODO(M2): implement every method of MessagesGateway
    _uow: UoW
    _helper: SqlRepositoryHelper[Message]
