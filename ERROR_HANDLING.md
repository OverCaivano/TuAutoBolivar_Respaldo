# ERROR_HANDLING.md


## Estrategia de Manejo de Errores en TuAutoBolivar


Este backend implementa un sistema robusto de manejo de errores con FastAPI:


### 1. **Validaciones automáticas de FastAPI y Pydantic**
- Campos requeridos.
- Tipos de datos (int, str, EmailStr, float, etc.).
- Restricciones (min_length, ge, le, etc.).


### 2. **HTTPException personalizada**
Se usa `fastapi.HTTPException` para devolver errores controlados:
```python
from fastapi import HTTPException


raise HTTPException(status_code=404, detail="Recurso no encontrado")
```


### 3. **Errores comunes manejados**
- **400 Bad Request** → Validación fallida (datos inválidos, email repetido, etc.).
- **401 Unauthorized** → Intento de acceso sin autenticación.
- **403 Forbidden** → Acceso denegado.
- **404 Not Found** → Usuario, auto u otro recurso inexistente.
- **500 Internal Server Error** → Error inesperado en el servidor.


### 4. **Middleware de manejo global de excepciones**
Se puede extender `middlewares/auth.py` o crear un middleware para capturar errores y loguearlos.


### 5. **Buenas prácticas**
- No exponer trazas internas en producción.
- Retornar siempre mensajes claros y consistentes.
- Usar logs para monitorear fallos.