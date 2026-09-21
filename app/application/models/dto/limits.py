from app.application.models.base import PydanticModel


class DailyUsage(PydanticModel):
    messages_used: int
    messages_limit: int  # 0 means unlimited
    voice_used: int
    voice_limit: int  # 0 means unlimited
