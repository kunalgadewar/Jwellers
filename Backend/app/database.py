# app/database.py

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# MySQL database URL in format: mysql+pymysql://<username>:<password>@<host>:<port>/<database_name>
DATABASE_URL = "mysql+pymysql://root:kunal%40123@localhost:3306/krishna_jewellers"

# Create the SQLAlchemy engine
engine = create_engine(DATABASE_URL)

# Create a session local class for DB interaction
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for our ORM models
Base = declarative_base()

# Add this to database.py

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
