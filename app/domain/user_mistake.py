from datetime import datetime

from sqlalchemy import ForeignKey, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.utils.custom_types import Int64

from .base import Base
from .enums.mistake_category import MistakeCategory
from .mixins.timestamp import NowFunc


class UserMistake(Base):
    __tablename__ = "user_mistakes"

    id: Mapped[Int64] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[Int64] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), index=True)
    original_text: Mapped[str] = mapped_column(Text())
    corrected_text: Mapped[str] = mapped_column(Text())
    explanation: Mapped[str] = mapped_column(Text())
    category: Mapped[MistakeCategory] = mapped_column()
    created_at: Mapped[datetime] = mapped_column(server_default=NowFunc)
