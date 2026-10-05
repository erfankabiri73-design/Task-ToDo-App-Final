from sqlalchemy.orm import Session
from models.user import UserModdel


class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_email(self, email: str) -> UserModdel | None:
        return self.db.query(UserModdel).filter_by(email=email).first()

    def get_by_id(self, user_id: int) -> UserModdel | None:
        return self.db.query(UserModdel).filter_by(id=user_id).first()

    def create_user(self, email: str, password: str) -> UserModdel:
        user = UserModdel(email=email)
        user.username = UserModdel.generate_random_username()
        user.set_password(password)

        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)

        return user