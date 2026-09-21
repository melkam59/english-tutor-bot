from datetime import datetime

from sqlalchemy import ForeignKey, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.utils.custom_types import Int32, Int64

from .base import Base
from .enums.message_role import MessageRole
from .mixins.timestamp import NowFunc


class Message(Base):
    __tablename__ = "messages"

    id: Mapped[Int64] = mapped_column(primary_key=True, autoincrement=True)
    conversation_id: Mapped[Int64] = mapped_column(
        ForeignKey("conversations.id", ondelete="CASCADE"),
        index=True,
    )
    role: Mapped[MessageRole] = mapped_column()
    text: Mapped[str] = mapped_column(Text())
    token_usage: Mapped[Int32] = mapped_column(default=0, server_default="0")
    created_at: Mapped[datetime] = mapped_column(server_default=NowFunc)
