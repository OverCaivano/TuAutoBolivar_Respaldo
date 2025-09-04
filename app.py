from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Importar rutas
from default.routes import router as default_router
from users import ruotes as users_routes  # ojo: archivo está con typo "ruotes.py"
from tasks import routes as tasks_routes

# Importar middleware de auth (si aplica en todas las rutas)
# from middlewares.auth import AuthMiddleware

# Crear instancia de FastAPI
app = FastAPI(
    title="TuAutoBolivar API",
    description="Backend para compra y venta de autos",
    version="1.0.0",
)

# Configuración de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Cambiar a dominios específicos en producción
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Middleware de autenticación global (opcional)
# app.add_middleware(AuthMiddleware)

# Incluir routers
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
