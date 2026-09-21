from aiogram.filters.callback_data import CallbackData


class CDStartAssessment(CallbackData, prefix="assess_start"):
    pass


class CDSkipAssessment(CallbackData, prefix="assess_skip"):
    pass


class CDAssessmentAnswer(CallbackData, prefix="assess_answer"):
    question_id: int
    option: int
