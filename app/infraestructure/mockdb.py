from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import Base

DATABASE_URL = "sqlite:///:memory:"

engine = create_engine(DATABASE_URL, echo=True)

def create_all_tables():
    Base.metadata.create_all(engine)

def get_db_session():
    SessionLocal = sessionmaker(engine)
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()