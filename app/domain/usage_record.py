from datetime import datetime
from decimal import Decimal

from sqlalchemy import ForeignKey, Numeric
from sqlalchemy.orm import Mapped, mapped_column

from app.utils.custom_types import Int32, Int64

from .base import Base
from .enums.request_type import RequestType
from .mixins.timestamp import NowFunc


class UsageRecord(Base):
    __tablename__ = "usage_records"

    id: Mapped[Int64] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[Int64] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), index=True)
    request_type: Mapped[RequestType] = mapped_column()
    input_tokens: Mapped[Int32] = mapped_column(default=0, server_default="0")
    output_tokens: Mapped[Int32] = mapped_column(default=0, server_default="0")
    estimated_cost: Mapped[Decimal] = mapped_column(Numeric(12, 6), default=0, server_default="0")
    created_at: Mapped[datetime] = mapped_column(server_default=NowFunc, index=True)
