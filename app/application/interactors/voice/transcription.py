from dataclasses import dataclass

from app.application.interactors.base import BaseInteractor
from app.application.ports.speech.gateway import (
    AudioConverter,
    SpeechToTextGateway,
    TextToSpeechGateway,
)
from app.application.ports.telegram.files import TelegramFiles
from app.domain.user import User


@dataclass(frozen=True)
class VoiceInteractor(BaseInteractor):
    user: User
    files: TelegramFiles
    converter: AudioConverter
    stt: SpeechToTextGateway
    tts: TextToSpeechGateway

    async def transcribe(self, file_id: str) -> str:
        # TODO(M4): download -> convert (ogg/opus -> supported format) -> STT,
        #  InvalidAudioError / TranscriptionError on failures
        raise NotImplementedError

    async def synthesize(self, text: str) -> bytes:
        # TODO(M4, optional): only when config.speech.tts_enabled
        raise NotImplementedError
