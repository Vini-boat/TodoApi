from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import Base

DATABASE_URL = "sqlite:///:memory:"

engine = create_engine(DATABASE_URL, echo=True, connect_args={"check_same_thread": False})

def create_all_tables():
    Base.metadata.create_all(engine)

def get_db_session():
    SessionLocal = sessionmaker(engine)
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()