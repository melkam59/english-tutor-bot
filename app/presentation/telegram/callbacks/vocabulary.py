from aiogram.filters.callback_data import CallbackData


class CDVocabularyList(CallbackData, prefix="vocab_list"):
    page: int = 0


class CDVocabularyAdd(CallbackData, prefix="vocab_add"):
    pass


class CDVocabularyDelete(CallbackData, prefix="vocab_del"):
    item_id: int


class CDVocabularyReview(CallbackData, prefix="vocab_review"):
    pass


class CDVocabularyAnswer(CallbackData, prefix="vocab_answer"):
    item_id: int
    is_correct: bool
