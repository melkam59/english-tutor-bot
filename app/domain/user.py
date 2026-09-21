from datetime import date, datetime
from typing import Optional

from aiogram import html
from aiogram.utils.link import create_tg_link
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.utils.custom_types import Int32, Int64

from .base import Base
from .enums.communication_format import CommunicationFormat
from .enums.english_level import EnglishLevel
from .enums.learning_goal import LearningGoal
from .enums.subscription import SubscriptionType
from .mixins.timestamp import TimestampMixin


class User(Base, TimestampMixin):
    __tablename__ = "users"

    # Telegram user ID
    id: Mapped[Int64] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column()
    username: Mapped[Optional[str]] = mapped_column()
    # Interface locale
    language: Mapped[str] = mapped_column(String(length=2))
    language_code: Mapped[Optional[str]] = mapped_column()

    # Learning profile
    native_language: Mapped[Optional[str]] = mapped_column(String(length=2))
    english_level: Mapped[Optional[EnglishLevel]] = mapped_column()
    learning_goal: Mapped[Optional[LearningGoal]] = mapped_column()
    communication_format: Mapped[Optional[CommunicationFormat]] = mapped_column()
    onboarded_at: Mapped[Optional[datetime]] = mapped_column()

    # Subscription
    subscription_type: Mapped[SubscriptionType] = mapped_column(
        default=SubscriptionType.FREE,
        server_default=SubscriptionType.FREE.name,
    )
    subscription_expires_at: Mapped[Optional[datetime]] = mapped_column()

    # Progress
    current_streak: Mapped[Int32] = mapped_column(default=0, server_default="0")
    last_study_date: Mapped[Optional[date]] = mapped_column()
    total_study_seconds: Mapped[Int32] = mapped_column(default=0, server_default="0")
    last_activity_at: Mapped[Optional[datetime]] = mapped_column()

    # The user blocked the bot
    blocked_at: Mapped[Optional[datetime]] = mapped_column()
    # An admin blocked the user
    banned_at: Mapped[Optional[datetime]] = mapped_column()

    @property
    def url(self) -> str:
        return create_tg_link("user", id=self.id)

    @property
    def mention(self) -> str:
        return html.link(value=self.name, link=self.url)

    @property
    def is_onboarded(self) -> bool:
        return self.onboarded_at is not None

    @property
    def is_banned(self) -> bool:
        return self.banned_at is not None
