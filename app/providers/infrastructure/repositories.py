from dishka import Provider, Scope, provide, provide_all

from app.application.ports.repositories.conversations import ConversationsGateway
from app.application.ports.repositories.lessons import LessonsGateway
from app.application.ports.repositories.messages import MessagesGateway
from app.application.ports.repositories.mistakes import MistakesGateway
from app.application.ports.repositories.usage import UsageGateway
from app.application.ports.repositories.users import UsersGateway
from app.application.ports.repositories.vocabulary import VocabularyGateway
from app.infrastructure.postgres.repositories.conversations import ConversationsRepository
from app.infrastructure.postgres.repositories.lessons import LessonsRepository
from app.infrastructure.postgres.repositories.messages import MessagesRepository
from app.infrastructure.postgres.repositories.mistakes import MistakesRepository
from app.infrastructure.postgres.repositories.usage import UsageRepository
from app.infrastructure.postgres.repositories.users import UsersRepository
from app.infrastructure.postgres.repositories.vocabulary import VocabularyRepository
from app.infrastructure.postgres.repository_helper import SqlRepositoryHelper
from app.infrastructure.postgres.uow import UoW


class RepositoriesProvider(Provider):
    scope = Scope.REQUEST

    database = provide_all(
        UoW,
        SqlRepositoryHelper,
        provide(UsersRepository, provides=UsersGateway),
        provide(ConversationsRepository, provides=ConversationsGateway),
        provide(MessagesRepository, provides=MessagesGateway),
        provide(MistakesRepository, provides=MistakesGateway),
        provide(VocabularyRepository, provides=VocabularyGateway),
        provide(LessonsRepository, provides=LessonsGateway),
        provide(UsageRepository, provides=UsageGateway),
    )
