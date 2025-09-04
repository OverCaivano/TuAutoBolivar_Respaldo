from pydantic import BaseModel, Field
from datetime import datetime

# ---------- Autos ----------

class AutoBase(BaseModel):
    marca: str = Field(..., min_length=2, max_length=100)
    modelo: str = Field(..., min_length=1, max_length=100)
    año: int = Field(..., ge=1900, le=datetime.now().year + 1)
    precio: int = Field(..., ge=0)
    descripcion: str | None = None


class AutoCreate(AutoBase):
    pass


class AutoUpdate(BaseModel):
    marca: str | None = Field(None, min_length=2, max_length=100)
    modelo: str | None = Field(None, min_length=1, max_length=100)
    año: int | None = Field(None, ge=1900, le=datetime.now().year + 1)
    precio: int | None = Field(None, ge=0)
    descripcion: str | None = None
    vendido: bool | None = None


class AutoResponse(AutoBase):
    id: int
    vendido: bool
    owner_id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
