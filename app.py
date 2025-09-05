from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from middlewares.auth import AuthMiddleware
from users.routes import router as users_router
from tasks.routes import router as autos_router
from default.routes import router as default_router
from TuAutoBolivar_Respaldo.users import routes as users_routes  # ojo: archivo está con typo "ruotes.py"
from tasks import routes as tasks_routes

app = FastAPI(
    title="TuAutoBolivar API",
    description="Backend para compra y venta de autos",
    version="1.0.0",
)

app.add_middleware(AuthMiddleware)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users_router)
app.include_router(autos_router)
app.include_router(default_router, prefix="/api", tags=["default"])
app.include_router(users_routes.router, prefix="/api/users", tags=["users"])
app.include_router(tasks_routes.router, prefix="/api/tasks", tags=["tasks"])

# Evento de inicio
@app.on_event("startup")
async def startup_event():
    print("🚀 TuAutoBolivar API iniciada")


# Evento de apagado
@app.on_event("shutdown")
async def shutdown_event():
    print("🛑 TuAutoBolivar API detenida")


# Health check básico
@app.get("/ping", tags=["health"])
async def ping():
    return {"status": "ok", "app": "TuAutoBolivar API"}
