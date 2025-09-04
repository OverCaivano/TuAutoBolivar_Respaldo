from pydantic import BaseModel, EmailStr, Field
from datetime import datetime

# ---------- Usuarios ----------

class UserBase(BaseModel):
    nombre: str = Field(..., min_length=2, max_length=100)
    email: EmailStr
    telefono: str | None = Field(None, max_length=20)


class UserCreate(UserBase):
    password: str = Field(..., min_length=6, max_length=100)


class UserUpdate(BaseModel):
    nombre: str | None = Field(None, min_length=2, max_length=100)
    telefono: str | None = Field(None, max_length=20)
    is_active: bool | None = None


class UserResponse(UserBase):
    id: int
    is_active: bool
    is_admin: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
