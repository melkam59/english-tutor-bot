from typing import Optional

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.utils.custom_types import Int64

from .base import Base
from .enums.practice_mode import PracticeMode, RolePlayScenario
from .mixins.timestamp import TimestampMixin


class Conversation(Base, TimestampMixin):
    __tablename__ = "conversations"

    id: Mapped[Int64] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[Int64] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), index=True)
    mode: Mapped[PracticeMode] = mapped_column()
    scenario: Mapped[Optional[RolePlayScenario]] = mapped_column()
    # Rolling summary of messages that no longer fit into the LLM context window
    summary: Mapped[Optional[str]] = mapped_column()
    is_active: Mapped[bool] = mapped_column(default=True, server_default="true")
