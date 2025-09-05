from fastapi import Request, HTTPException
from starlette.middleware.base import BaseHTTPMiddleware

class AuthMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        # Ejemplo de token estático (mejor reemplazar con JWT)
        token = request.headers.get("Authorization")

        if not token or token != "Bearer secret-token":
            # Permitimos el acceso a rutas públicas
            if request.url.path in ["/", "/health", "/docs", "/openapi.json"]:
                return await call_next(request)
            raise HTTPException(status_code=401, detail="No autorizado")

        response = await call_next(request)
        return response
