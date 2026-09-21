from enum import StrEnum, auto


# noinspection PyEnum
class MistakeCategory(StrEnum):
    GRAMMAR = auto()
    VOCABULARY = auto()
    WORD_ORDER = auto()
    ARTICLES = auto()
    PREPOSITIONS = auto()
    VERB_TENSE = auto()
    SPELLING = auto()
    STYLE = auto()
