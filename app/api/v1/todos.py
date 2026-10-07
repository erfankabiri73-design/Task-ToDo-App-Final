from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.api.v1.auth import get_authenticated_user
from app.models.user import UserModdel

from app.repositories.todo_repository import TodoRepository
from app.services.todo_services import TodoService

from app.schemas.todo import (
    TodoCreateSchema,
    TodoUpdateSchema,
    TodoResponseSchema,
)


router = APIRouter(
    prefix="/todos",
    tags=["Todos"],
)


def get_todo_service(
    db: Session = Depends(get_db),
) -> TodoService:
    todo_repo = TodoRepository(db)
    return TodoService(todo_repo)


@router.post(
    "/",
    response_model=TodoResponseSchema,
    status_code=status.HTTP_201_CREATED,
)
def create_todo(
    request: TodoCreateSchema,
    current_user: UserModdel = Depends(get_authenticated_user),
    todo_service: TodoService = Depends(get_todo_service),
):
    return todo_service.create_todo(
        request=request,
        user_id=current_user.id,
    )


@router.get(
    "/",
    response_model=list[TodoResponseSchema],
)
def get_todos(
    current_user: UserModdel = Depends(get_authenticated_user),
    todo_service: TodoService = Depends(get_todo_service),
):
    return todo_service.get_all_todos(
        user_id=current_user.id,
    )


@router.get(
    "/{todo_id}",
    response_model=TodoResponseSchema,
)
def get_todo(
    todo_id: int,
    current_user: UserModdel = Depends(get_authenticated_user),
    todo_service: TodoService = Depends(get_todo_service),
):
    return todo_service.get_todo(
        todo_id=todo_id,
        user_id=current_user.id,
    )


@router.patch(
    "/{todo_id}",
    response_model=TodoResponseSchema,
)
def update_todo(
    todo_id: int,
    request: TodoUpdateSchema,
    current_user: UserModdel = Depends(get_authenticated_user),
    todo_service: TodoService = Depends(get_todo_service),
):
    return todo_service.update_todo(
        todo_id=todo_id,
        request=request,
        user_id=current_user.id,
    )


@router.delete(
    "/{todo_id}",
    status_code=status.HTTP_200_OK,
)
def delete_todo(
    todo_id: int,
    current_user: UserModdel = Depends(get_authenticated_user),
    todo_service: TodoService = Depends(get_todo_service),
):
    return todo_service.delete_todo(
        todo_id=todo_id,
        user_id=current_user.id,
    )