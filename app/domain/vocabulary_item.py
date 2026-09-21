from datetime import datetime
from typing import Optional

from sqlalchemy import ForeignKey, Text, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column

from app.utils.custom_types import Int32, Int64

from .base import Base
from .mixins.timestamp import NowFunc


class VocabularyItem(Base):
    __tablename__ = "vocabulary_items"
    __table_args__ = (UniqueConstraint("user_id", "phrase"),)

    id: Mapped[Int64] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[Int64] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), index=True)
    phrase: Mapped[str] = mapped_column()
    translation: Mapped[str] = mapped_column()
    example: Mapped[Optional[str]] = mapped_column(Text())
    correct_count: Mapped[Int32] = mapped_column(default=0, server_default="0")
    incorrect_count: Mapped[Int32] = mapped_column(default=0, server_default="0")
    next_review_at: Mapped[datetime] = mapped_column(server_default=NowFunc, index=True)
    created_at: Mapped[datetime] = mapped_column(server_default=NowFunc)
