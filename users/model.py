from sqlalchemy import Column, Integer, String, Boolean, DateTime, func
from sqlalchemy.orm import relationship
from config.basemodel import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    email = Column(String(150), unique=True, nullable=False, index=True)
    hashed_password = Column(String(255), nullable=False)
    telefono = Column(String(20), nullable=True)
    is_active = Column(Boolean, default=True, server_default="1")
    is_admin = Column(Boolean, default=False, server_default="0")

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    # Relación con autos publicados (si aplicamos compra/venta de autos)
    autos = relationship("Task", back_populates="owner", cascade="all, delete-orphan")
