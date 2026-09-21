from app.application.errors.base import AppError


class LimitError(AppError):
    pass


class DailyLimitReachedError(LimitError):
    pass


class VoiceLimitReachedError(LimitError):
    pass


class VoiceTooLongError(LimitError):
    pass


class InputTooLongError(LimitError):
    pass


class PremiumRequiredError(LimitError):
    pass
