import os

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

###
# Database Configuration
###

SQLALCHEMY_DATABASE_URL = "postgresql://vaibhav:vaibhav123@localhost/vaibhav_db"

engine = create_engine(
    os.getenv("DB_URL", SQLALCHEMY_DATABASE_URL),
    future=True,
    echo=True,  # optional: shows SQL in console (good for learning)
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
