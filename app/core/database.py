<<<<<<< HEAD
=======
<<<<<<< Updated upstream
=======
>>>>>>> alembic,env,init,databse
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from .config import settings

DATABASE_URL = settings.DATABASE_URL

engine = create_engine(
    DATABASE_URL,
<<<<<<< HEAD
    # connect_args={"check_same_thread": False},  # only for sqlite
=======
     connect_args={"check_same_thread": False},  # only for sqlite
>>>>>>> alembic,env,init,databse
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        # Always close the session to release the connection
<<<<<<< HEAD
        db.close()
=======
        db.close()
>>>>>>> Stashed changes
>>>>>>> alembic,env,init,databse
