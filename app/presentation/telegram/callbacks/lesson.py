from aiogram.filters.callback_data import CallbackData


class CDNewLesson(CallbackData, prefix="lesson_new"):
    pass


class CDLessonNextPractice(CallbackData, prefix="lesson_next"):
    lesson_id: int
