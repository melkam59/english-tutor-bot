from dishka import Provider, Scope, provide

from app.application.models.config import AppConfig
from app.application.ports.llm.gateway import LLMGateway
from app.application.ports.speech.gateway import (
    AudioConverter,
    SpeechToTextGateway,
    TextToSpeechGateway,
)
from app.infrastructure.llm.factory import create_llm_gateway
from app.infrastructure.speech.converter import FFmpegAudioConverter
from app.infrastructure.speech.openai import OpenAISpeechToText, OpenAITextToSpeech


class AIProvider(Provider):
    """LLM and speech providers are selected by LLM_PROVIDER / SPEECH_PROVIDER env variables."""

    scope = Scope.APP

    @provide
    def provide_llm(self, config: AppConfig) -> LLMGateway:
        return create_llm_gateway(config=config.llm)

    @provide
    def provide_stt(self, config: AppConfig) -> SpeechToTextGateway:
        return OpenAISpeechToText(config=config.speech)

    @provide
    def provide_tts(self, config: AppConfig) -> TextToSpeechGateway:
        return OpenAITextToSpeech(config=config.speech)

    @provide
    def provide_audio_converter(self) -> AudioConverter:
        return FFmpegAudioConverter()
