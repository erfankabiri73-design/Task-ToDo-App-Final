<<<<<<< HEAD

=======
<<<<<<< Updated upstream
=======
from  app.core.database  import Base
>>>>>>> alembic,env,init,databse
from sqlalchemy import Column,String,Integer,Boolean,DateTime,func
import enum

class UserTypes():
    Admin      = "admin"
    Developer  = "developer"
    Supervisor = "supervisor"

class UserModdel(Base):
    __tablename__ = "users"
    id          = Column(Integer,primary_key=True,autoincrement=True)
    username    = Column(String,unique=True,nullable=False)
    email       = Column(String,unique=True,nullable=False)
    password    = Column(String,nullable=False)
    type        = Column(String,default=UserTypes.Developer)
<<<<<<< HEAD
    is_verified = Column(Boolean,server_default="false")
    is_active   = Column(Boolean,server_default="true")
>>>>>>> alembic,env,init,databse
    created_date= Column(DateTime(timezone=True),default=func.now())
    updated_date= Column(DateTime(timezone=True),server_default=func.now(),
                                                server_onupdate=func.now())


<<<<<<< HEAD
=======
>>>>>>> Stashed changes
>>>>>>> alembic,env,init,databse
