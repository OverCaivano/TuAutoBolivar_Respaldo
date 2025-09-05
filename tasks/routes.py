from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from config.cnx import get_db
from tasks import dto as auto_dto
from tasks.services import (
    create_auto, get_autos, get_auto, update_auto, delete_auto
)

router = APIRouter(prefix="/autos", tags=["autos"])

@router.post("", response_model=auto_dto.AutoResponse)
def api_create_auto(auto_in: auto_dto.AutoCreate, owner_id: int, db: Session = Depends(get_db)):
    # owner_id llega como query param, ej: POST /autos?owner_id=1
    return create_auto(db, auto_in, owner_id)

@router.get("", response_model=list[auto_dto.AutoResponse])
def api_get_autos(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_autos(db, skip, limit)

@router.get("/{auto_id}", response_model=auto_dto.AutoResponse)
def api_get_auto(auto_id: int, db: Session = Depends(get_db)):
    return get_auto(db, auto_id)

@router.put("/{auto_id}", response_model=auto_dto.AutoResponse)
def api_update_auto(auto_id: int, auto_in: auto_dto.AutoUpdate, db: Session = Depends(get_db)):
    return update_auto(db, auto_id, auto_in)

@router.delete("/{auto_id}")
def api_delete_auto(auto_id: int, db: Session = Depends(get_db)):
    return delete_auto(db, auto_id)
