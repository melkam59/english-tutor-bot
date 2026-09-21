from enum import StrEnum, auto


# noinspection PyEnum
class MessageRole(StrEnum):
    SYSTEM = auto()
    USER = auto()
    ASSISTANT = auto()
