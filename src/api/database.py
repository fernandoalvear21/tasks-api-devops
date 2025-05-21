from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()

# Definimos la ruta base del proyecto (un nivel arriba de src)
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Por defecto, usamos SQLite para desarrollo con ruta absoluta
DATABASE_URL = os.getenv("DATABASE_URL", f"sqlite:///{BASE_DIR}/tasks.db")

engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()