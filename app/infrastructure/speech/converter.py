from dataclasses import dataclass

from app.application.ports.speech.gateway import AudioConverter


@dataclass
class FFmpegAudioConverter(AudioConverter):
    """Telegram voice messages are OGG/Opus, ffmpeg is installed in the Docker image."""

    async def to_supported_format(self, audio: bytes, source_format: str) -> tuple[bytes, str]:
        # TODO(M4): asyncio.create_subprocess_exec("ffmpeg", ...) via stdin/stdout,
        #  raise InvalidAudioError on a non-zero exit code
        raise NotImplementedError
