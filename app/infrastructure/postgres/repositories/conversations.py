from dataclasses import dataclass

from app.application.ports.repositories.conversations import ConversationsGateway
from app.domain.conversation import Conversation
from app.infrastructure.postgres.repository_helper import SqlRepositoryHelper
from app.infrastructure.postgres.uow import UoW


@dataclass
class ConversationsRepository(ConversationsGateway):
    # TODO(M2): implement every method of ConversationsGateway
    _uow: UoW
    _helper: SqlRepositoryHelper[Conversation]
