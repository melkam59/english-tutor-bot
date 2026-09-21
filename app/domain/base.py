import enum
from datetime import date, datetime

from sqlalchemy import BigInteger, Date, DateTime, Enum, Integer, SmallInteger, String
from sqlalchemy.dialects.postgresql import ARRAY, JSON
from sqlalchemy.orm import DeclarativeBase, registry

from app.utils.custom_types import DictStrAny, Int16, Int32, Int64


class Base(DeclarativeBase):
    registry = registry(
        type_annotation_map={
            Int16: SmallInteger(),
            Int32: Integer(),
            Int64: BigInteger(),
            DictStrAny: JSON(),
            list[str]: ARRAY(String()),
            datetime: DateTime(timezone=True),
            date: Date(),
            # Stored as VARCHAR so adding enum members never requires a migration
            enum.Enum: Enum(enum.Enum, native_enum=False, length=32),
        }
    )
