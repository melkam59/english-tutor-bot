from pydantic import BaseModel

from .common import CommonConfig
from .limits import LimitsConfig
from .llm import LLMConfig
from .postgres import PostgresConfig
from .redis import RedisConfig
from .server import ServerConfig
from .speech import SpeechConfig
from .sql_alchemy import SQLAlchemyConfig
from .telegram import TelegramConfig


class AppConfig(BaseModel):
    telegram: TelegramConfig
    postgres: PostgresConfig
    sql_alchemy: SQLAlchemyConfig
    redis: RedisConfig
    server: ServerConfig
    common: CommonConfig
    llm: LLMConfig
    speech: SpeechConfig
    limits: LimitsConfig
