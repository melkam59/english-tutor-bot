from typing import Protocol


class SpeechToTextGateway(Protocol):
    async def transcribe(self, audio: bytes, filename: str, language: str = "en") -> str: ...


class TextToSpeechGateway(Protocol):
    async def synthesize(self, text: str) -> bytes: ...


class AudioConverter(Protocol):
    async def to_supported_format(self, audio: bytes, source_format: str) -> tuple[bytes, str]:
        """:return: converted audio and its filename (extension matters for STT APIs)"""
        ...
