from core.database import Base
from sqlalchemy import Column, String, Integer, Boolean, DateTime, ForeignKey, func
import enum



class TodoPriority(str, enum.Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


class TodoModel(Base):
    __tablename__ = "todos"

    id = Column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    title = Column(
        String,
        nullable=False
    )

    description = Column(
        String,
        nullable=True
    )

    priority = Column(
        String,
        default=TodoPriority.MEDIUM,
        nullable=False
    )

    is_completed = Column(
        Boolean,
        default=False
    )

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )

    created_date = Column(
        DateTime(timezone=True),
        default=func.now()
    )

    updated_date = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        server_onupdate=func.now()
    )