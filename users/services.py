from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from users import model as user_model, dto as user_dto

def create_user(db: Session, user_in: user_dto.UserCreate):
    existing = db.query(user_model.User).filter(user_model.User.email == user_in.email).first()
    if existing:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email ya registrado")
    user = user_model.User(**user_in.dict())
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def get_users(db: Session, skip: int = 0, limit: int = 10):
    return db.query(user_model.User).offset(skip).limit(limit).all()

def get_user(db: Session, user_id: int):
    user = db.query(user_model.User).filter(user_model.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return user

def update_user(db: Session, user_id: int, user_in: user_dto.UserUpdate):
    user = get_user(db, user_id)
    for k, v in user_in.dict(exclude_unset=True).items():
        setattr(user, k, v)
    db.commit()
    db.refresh(user)
    return user

def delete_user(db: Session, user_id: int):
    user = get_user(db, user_id)
    db.delete(user)
    db.commit()
    return {"detail": "Usuario eliminado"}