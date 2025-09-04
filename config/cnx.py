from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
import os

# Leer URL de conexión desde variable de entorno o usar SQLite por defecto
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./mibase.db")

# Configuración para SQLite (evitar problemas con threads)
connect_args = {"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {}

# Crear motor SQLAlchemy
engine = create_engine(DATABASE_URL, connect_args=connect_args, echo=True)

# Crear sesión
SessionLocal = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

# Dependencia para obtener sesión en rutas
# (se usará en FastAPI con Depends)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
