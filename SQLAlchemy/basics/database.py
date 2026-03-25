from sqlalchemy import create_engine #help to connect the python with database
from sqlalchemy.orm import DeclarativeBase , sessionmaker


DATABASE_URL = "sqlite:///./mydb.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread":False}
)

class Base(DeclarativeBase):
    pass

SessionLocal = sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False
)

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()