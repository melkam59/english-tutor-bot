from aiogram.fsm.state import State, StatesGroup


class OnboardingSG(StatesGroup):
    native_language = State()
    english_level = State()
    learning_goal = State()
    communication_format = State()


class AssessmentSG(StatesGroup):
    multiple_choice = State()
    written_answer = State()


class LessonSG(StatesGroup):
    waiting_answer = State()


class VocabularySG(StatesGroup):
    waiting_phrase = State()
    reviewing = State()


class BroadcastSG(StatesGroup):
    waiting_text = State()
    confirmation = State()
