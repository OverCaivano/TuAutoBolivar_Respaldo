from fastapi import APIRouter

router = APIRouter(prefix="", tags=["default"])

@router.get("/")
def root():
    return {"message": "Bienvenido a la API de TuAutoBolivar 🚗"}

@router.get("/health")
def health_check():
    return {"status": "ok"}
