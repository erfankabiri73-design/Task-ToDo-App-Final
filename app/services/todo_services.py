from fastapi import HTTPException, status

from app.repositories.todo_repository import TodoRepository
from app.schemas.todo import TodoCreateSchema, TodoUpdateSchema


class TodoService:
    def __init__(self, todo_repo: TodoRepository):
        self.todo_repo = todo_repo

    def create_todo(
        self,
        request: TodoCreateSchema,
        user_id: int,
    ):
        return self.todo_repo.create_todo(
            title=request.title,
            description=request.description,
            priority=request.priority.value,
            user_id=user_id,
        )

    def get_all_todos(self, user_id: int):
        return self.todo_repo.get_all_by_user(
            user_id=user_id
        )

    def get_todo(self, todo_id: int, user_id: int):
        todo = self.todo_repo.get_by_id(
            todo_id=todo_id,
            user_id=user_id,
        )

        if not todo:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Todo not found",
            )

        return todo

    def update_todo(
        self,
        todo_id: int,
        request: TodoUpdateSchema,
        user_id: int,
    ):
        todo = self.todo_repo.get_by_id(
            todo_id=todo_id,
            user_id=user_id,
        )

        if not todo:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Todo not found",
            )

        updates = request.model_dump(
            exclude_unset=True
        )

        if "priority" in updates:
            updates["priority"] = updates["priority"].value

        return self.todo_repo.update_todo(
            todo=todo,
            **updates,
        )

    def delete_todo(
        self,
        todo_id: int,
        user_id: int,
    ):
        todo = self.todo_repo.get_by_id(
            todo_id=todo_id,
            user_id=user_id,
        )

        if not todo:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Todo not found",
            )

        self.todo_repo.delete_todo(todo)

        return {
            "detail": "Todo deleted successfully"
        }