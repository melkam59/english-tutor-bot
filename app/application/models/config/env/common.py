from typing import Optional

from pydantic import SecretStr

from .base import EnvSettings


class CommonConfig(EnvSettings, env_prefix="COMMON_"):
    admin_chat_id: int
    sentry_dsn: Optional[SecretStr] = None
