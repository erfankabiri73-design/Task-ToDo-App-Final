from sqlalchemy.orm import Session

from app.models.todo import TodoModel


class TodoRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_todo(
        self,
        title: str,
        description: str | None,
        priority: str,
        user_id: int,
    ) -> TodoModel:

        todo = TodoModel(
            title=title,
            description=description,
            priority=priority,
            user_id=user_id,
        )

        self.db.add(todo)
        self.db.commit()
        self.db.refresh(todo)

        return todo

    def get_by_id(
        self,
        todo_id: int,
        user_id: int,
    ) -> TodoModel | None:

        return (
            self.db.query(TodoModel)
            .filter_by(
                id=todo_id,
                user_id=user_id,
            )
            .first()
        )

    def get_all_by_user(
        self,
        user_id: int,
    ) -> list[TodoModel]:

        return (
            self.db.query(TodoModel)
            .filter_by(user_id=user_id)
            .all()
        )

    def update_todo(
        self,
        todo: TodoModel,
        **updates,
    ) -> TodoModel:

        for field, value in updates.items():
            setattr(todo, field, value)

        self.db.commit()
        self.db.refresh(todo)

        return todo

    def delete_todo(
        self,
        todo: TodoModel,
    ) -> None:

        self.db.delete(todo)
        self.db.commit()