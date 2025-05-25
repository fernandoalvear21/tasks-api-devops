from src.api.database import engine
from src.api.models.task import Base

def init_db():
    Base.metadata.create_all(bind=engine)
    print("Base de datos inicializada correctamente")

if __name__ == "__main__":
    init_db()