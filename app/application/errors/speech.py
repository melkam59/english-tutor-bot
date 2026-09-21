from app.application.errors.base import AppError


class SpeechError(AppError):
    pass


class InvalidAudioError(SpeechError):
    pass


class TranscriptionError(SpeechError):
    pass
