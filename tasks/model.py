from sqlalchemy import Column, Integer, String, Text, Boolean, DateTime, ForeignKey, func
from sqlalchemy.orm import relationship
from config.basemodel import Base

class Auto(Base):
    __tablename__ = "autos"

    id = Column(Integer, primary_key=True, index=True)
    marca = Column(String(100), nullable=False)
    modelo = Column(String(100), nullable=False)
    año = Column(Integer, nullable=False)
    precio = Column(Integer, nullable=False)
    descripcion = Column(Text, nullable=True)
    vendido = Column(Boolean, default=False, server_default="0")

    owner_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    owner = relationship("User", back_populates="autos")

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
