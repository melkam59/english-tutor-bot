from app.application.errors.base import AppError


class LLMError(AppError):
    pass


class LLMTimeoutError(LLMError):
    pass


class LLMRateLimitError(LLMError):
    pass


class LLMInvalidResponseError(LLMError):
    """The model returned something that does not match the expected schema."""
