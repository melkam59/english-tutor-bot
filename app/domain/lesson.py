from datetime import datetime
from typing import Optional

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.utils.custom_types import DictStrAny, Int64

from .base import Base
from .enums.english_level import EnglishLevel
from .mixins.timestamp import NowFunc


class Lesson(Base):
    __tablename__ = "lessons"

    id: Mapped[Int64] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[Int64] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), index=True)
    topic: Mapped[str] = mapped_column()
    level: Mapped[EnglishLevel] = mapped_column()
    # Explanation, examples, exercise, user answer, AI feedback, extra practice question
    content: Mapped[DictStrAny] = mapped_column()
    created_at: Mapped[datetime] = mapped_column(server_default=NowFunc)
    completed_at: Mapped[Optional[datetime]] = mapped_column()

    @property
    def is_completed(self) -> bool:
        return self.completed_at is not None
