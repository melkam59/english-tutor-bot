from enum import StrEnum, auto


# noinspection PyEnum
class PracticeMode(StrEnum):
    GENERAL = auto()
    TRAVEL = auto()
    BUSINESS = auto()
    JOB_INTERVIEW = auto()
    IT = auto()
    GRAMMAR = auto()
    VOCABULARY = auto()
    ROLE_PLAY = auto()


# noinspection PyEnum
class RolePlayScenario(StrEnum):
    RESTAURANT = auto()
    HOTEL_CHECK_IN = auto()
    RECRUITER = auto()
    WORK_MEETING = auto()
    CUSTOMER = auto()
    AIRPORT_SECURITY = auto()
