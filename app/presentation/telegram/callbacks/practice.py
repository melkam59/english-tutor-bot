from aiogram.filters.callback_data import CallbackData

from app.domain.enums.practice_mode import PracticeMode, RolePlayScenario


class CDPracticeMode(CallbackData, prefix="practice_mode"):
    mode: PracticeMode


class CDRolePlayScenario(CallbackData, prefix="scenario"):
    scenario: RolePlayScenario


class CDStopPractice(CallbackData, prefix="practice_stop"):
    pass


class CDSaveWord(CallbackData, prefix="save_word"):
    message_id: int
