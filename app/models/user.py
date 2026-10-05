
from core.database  import Base
from sqlalchemy import Column,String,Integer,Boolean,DateTime,func
from passlib.context import CryptContext
import enum
import secrets
import string


class UserTypes(str, enum.Enum):
    Admin      = "admin"
    Developer  = "developer"
    Supervisor = "supervisor"

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class UsernameMixin:
    username: str

    @classmethod
    def generate_random_username(cls, length: int = 10) -> str:
        chars = string.ascii_lowercase + string.digits
        return "".join(secrets.choice(chars) for _ in range(length))


class PasswordMixin:
    password: str

    def verify_password(self, plain_password: str) -> bool:
        """Verifies the given password against the stored hash."""
        return pwd_context.verify(plain_password, self.password)

    def set_password(self, plain_text: str) -> None:
        print(pwd_context.hash(plain_text))
        self.password = pwd_context.hash(plain_text)

class UserModdel(Base, PasswordMixin, UsernameMixin):
    __tablename__ = "users"
    id          = Column(Integer,primary_key=True,autoincrement=True)
    username    = Column(String,unique=True,nullable=False)
    email       = Column(String,unique=True,nullable=False)
    password    = Column(String,nullable=False)
    type        = Column(String,default=UserTypes.Developer)
    is_verified = Column(Boolean,server_default="false")
    is_active   = Column(Boolean,server_default="true")
    created_date= Column(DateTime(timezone=True),default=func.now())
    updated_date= Column(DateTime(timezone=True),server_default=func.now(),
                                                server_onupdate=func.now())


"""
class RefreshToken(Base):
    __tablename__ = "refresh_tokens"

    id = Column(Integer,primary_key=True)
    token_hash: Column(String,unique=True, index=True)
    user_id = int = Column(Integer,ForeignKey("users.id"))
    device_id = Column(String)
    expires_at =Column(datetime)
    revoked_at =Column() datetime | None]
    created_at = Column() datetime
"""