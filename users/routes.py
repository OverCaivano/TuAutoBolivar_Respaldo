from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from config.cnx import get_db
from users import dto as user_dto
from users.services import (
    create_user, get_users, get_user, update_user, delete_user
)

router = APIRouter(prefix="/users", tags=["users"])

@router.post("", response_model=user_dto.UserResponse)
def api_create_user(user_in: user_dto.UserCreate, db: Session = Depends(get_db)):
    return create_user(db, user_in)

@router.get("", response_model=list[user_dto.UserResponse])
def api_get_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_users(db, skip, limit)

@router.get("/{user_id}", response_model=user_dto.UserResponse)
def api_get_user(user_id: int, db: Session = Depends(get_db)):
    return get_user(db, user_id)

@router.put("/{user_id}", response_model=user_dto.UserResponse)
def api_update_user(user_id: int, user_in: user_dto.UserUpdate, db: Session = Depends(get_db)):
    return update_user(db, user_id, user_in)

@router.delete("/{user_id}")
def api_delete_user(user_id: int, db: Session = Depends(get_db)):
    return delete_user(db, user_id)
