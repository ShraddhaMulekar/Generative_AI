from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# DB URL
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

# create engine
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

# session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# base class
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()