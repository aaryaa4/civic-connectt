import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# This now reads the database URL from the Railway environment variable
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")

# The connect_args is removed as it's only for SQLite
engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
       yield db
    finally:
        db.close()