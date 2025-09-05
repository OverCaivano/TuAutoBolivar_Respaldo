from sqlalchemy.orm import Session
from fastapi import HTTPException
from tasks import model as auto_model, dto as auto_dto

def create_auto(db: Session, auto_in: auto_dto.AutoCreate, owner_id: int):
    auto = auto_model.Auto(**auto_in.dict(), owner_id=owner_id)
    db.add(auto)
    db.commit()
    db.refresh(auto)
    return auto

def get_autos(db: Session, skip: int = 0, limit: int = 10):
    return db.query(auto_model.Auto).offset(skip).limit(limit).all()

def get_auto(db: Session, auto_id: int):
    auto = db.query(auto_model.Auto).filter(auto_model.Auto.id == auto_id).first()
    if not auto:
        raise HTTPException(status_code=404, detail="Auto no encontrado")
    return auto

def update_auto(db: Session, auto_id: int, auto_in: auto_dto.AutoUpdate):
    auto = get_auto(db, auto_id)
    for k, v in auto_in.dict(exclude_unset=True).items():
        setattr(auto, k, v)
    db.commit()
    db.refresh(auto)
    return auto

def delete_auto(db: Session, auto_id: int):
    auto = get_auto(db, auto_id)
    db.delete(auto)
    db.commit()
    return {"detail": "Auto eliminado"}
