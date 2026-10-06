from datetime import datetime
from enum import Enum

from pydantic import BaseModel, Field, ConfigDict


class TodoPriority(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


class TodoCreateSchema(BaseModel):
    title: str = Field(
        ...,
        min_length=1,
        max_length=200,
        examples=["Finish FastAPI project"],
    )

    description: str | None = Field(
        default=None,
        max_length=1000,
        examples=["Complete the Todo CRUD endpoints"],
    )

    priority: TodoPriority = Field(
        default=TodoPriority.MEDIUM,
        examples=["high"],
    )

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "title": "Finish FastAPI project",
                "description": "Complete the Todo CRUD endpoints",
                "priority": "high",
            }
        }
    )


class TodoUpdateSchema(BaseModel):
    title: str | None = Field(
        default=None,
        min_length=1,
        max_length=200,
    )

    description: str | None = Field(
        default=None,
        max_length=1000,
    )

    priority: TodoPriority | None = None

    is_completed: bool | None = None


class TodoResponseSchema(BaseModel):
    id: int
    title: str
    description: str | None
    priority: TodoPriority
    is_completed: bool
    user_id: int
    created_date: datetime
    updated_date: datetime | None

    model_config = ConfigDict(
        from_attributes=True
    )