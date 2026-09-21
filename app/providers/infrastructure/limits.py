from aiogram import Bot
from dishka import Provider, Scope, provide

from app.application.ports.limits.rate_limiter import Throttler, UsageCounter
from app.application.ports.telegram.broadcaster import Broadcaster
from app.application.ports.telegram.files import TelegramFiles
from app.infrastructure.redis.limits import RedisThrottler, RedisUsageCounter
from app.infrastructure.redis.repository import RedisRepository
from app.infrastructure.telegram.broadcaster import BroadcasterImpl
from app.infrastructure.telegram.files import TelegramFilesImpl


class LimitsProvider(Provider):
    scope = Scope.APP

    @provide
    def provide_usage_counter(self, repository: RedisRepository) -> UsageCounter:
        return RedisUsageCounter(repository=repository)

    @provide
    def provide_throttler(self, repository: RedisRepository) -> Throttler:
        return RedisThrottler(repository=repository)


class TelegramAdaptersProvider(Provider):
    scope = Scope.APP

    @provide
    def provide_files(self, bot: Bot) -> TelegramFiles:
        return TelegramFilesImpl(bot=bot)

    @provide
    def provide_broadcaster(self, bot: Bot) -> Broadcaster:
        return BroadcasterImpl(bot=bot)
