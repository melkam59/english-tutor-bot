from enum import StrEnum, auto


# noinspection PyEnum
class RequestType(StrEnum):
    CHAT = auto()
    ASSESSMENT = auto()
    LESSON = auto()
    VOCABULARY = auto()
    SUMMARY = auto()
    SPEECH_TO_TEXT = auto()
    TEXT_TO_SPEECH = auto()
