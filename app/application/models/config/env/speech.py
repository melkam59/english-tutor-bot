from enum import StrEnum, auto

from pydantic import SecretStr

from .base import EnvSettings


# noinspection PyEnum
class SpeechProviderType(StrEnum):
    OPENAI = auto()


class SpeechConfig(EnvSettings, env_prefix="SPEECH_"):
    provider: SpeechProviderType
    api_key: SecretStr
    stt_model: str
    request_timeout: float = 60.0
    # USD per minute of transcribed audio
    stt_price_per_minute: float = 0.0
    # Optional audio replies
    tts_enabled: bool = False
    tts_model: str = ""
    tts_voice: str = ""
