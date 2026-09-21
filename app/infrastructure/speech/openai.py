from dataclasses import dataclass

from app.application.models.config.env import SpeechConfig
from app.application.ports.speech.gateway import SpeechToTextGateway, TextToSpeechGateway


@dataclass
class OpenAISpeechToText(SpeechToTextGateway):
    config: SpeechConfig

    async def transcribe(self, audio: bytes, filename: str, language: str = "en") -> str:
        # TODO(M4): audio.transcriptions.create(model=config.stt_model), TranscriptionError
        raise NotImplementedError


@dataclass
class OpenAITextToSpeech(TextToSpeechGateway):
    config: SpeechConfig

    async def synthesize(self, text: str) -> bytes:
        # TODO(M4, optional): audio.speech.create(model=config.tts_model, voice=config.tts_voice)
        raise NotImplementedError
