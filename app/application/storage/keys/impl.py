from dataclasses import dataclass

from app.application.storage.keys.base import StorageKey


@dataclass(kw_only=True, frozen=True)
class WebhookLockKey(StorageKey[str], prefix="webhook_lock", type=str):
    """Значение — хэш текущего установленного вебхука для этого bot_id."""

    bot_id: int


@dataclass(kw_only=True, frozen=True)
class CommandsLockKey(StorageKey[str], prefix="commands_lock", type=str):
    """Значение — хэш текущего набора команд бота для этого bot_id."""

    bot_id: int


@dataclass(kw_only=True, frozen=True)
class DailyMessagesKey(StorageKey[int], prefix="daily_messages", type=int):
    """Number of AI messages the user has sent on the given day (ISO date)."""

    user_id: int
    day: str


@dataclass(kw_only=True, frozen=True)
class DailyVoiceMessagesKey(StorageKey[int], prefix="daily_voice", type=int):
    """Number of voice messages the user has sent on the given day (ISO date)."""

    user_id: int
    day: str


@dataclass(kw_only=True, frozen=True)
class ThrottleKey(StorageKey[int], prefix="throttle", type=int):
    user_id: int


@dataclass(kw_only=True, frozen=True)
class UpdateDedupKey(StorageKey[int], prefix="update_dedup", type=int):
    bot_id: int
    update_id: int
