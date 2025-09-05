# SERVICES_VALIDATION.md


## Validaciones implementadas en TuAutoBolivar


### 1. **Usuarios (`users/dto.py`)**
- `name`: mínimo 3 caracteres.
- `email`: validación con `EmailStr`.
- `hashed_password`: requerido al crear usuario.


### 2. **Autos (`tasks/dto.py`)**
- `marca` y `modelo`: no vacíos.
- `anio`: entero positivo (ejemplo: `ge=1900`).
- `precio`: número positivo.
- `vendido`: booleano (por defecto `False`).


### 3. **Relaciones**
- Cada `Auto` requiere un `owner_id` válido (usuario existente).


### 4. **Reglas adicionales de negocio**
- No se permiten emails duplicados en usuarios.
- No se pueden registrar autos duplicados con misma marca, modelo y año para el mismo dueño.


### 5. **Prácticas de validación recomendadas**
- Validar en **DTOs (entrada de datos)**.
- Validar en **Services (reglas de negocio)**.
- Mantener las validaciones centralizadas y documentadas.