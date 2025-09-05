from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context
import sys
import os

# Agregamos la carpeta raíz al path para que reconozca los módulos
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from config.cnx import SQLALCHEMY_DATABASE_URL
from config.basemodel import Base
from users.model import User
from tasks.model import Auto

# Configuración Alembic
config = context.config

# Configuración de logging
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Metadatos para autogenerar migraciones
target_metadata = Base.metadata

def run_migrations_offline():
    """Ejecutar migraciones en modo offline."""
    url = SQLALCHEMY_DATABASE_URL
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    """Ejecutar migraciones en modo online."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
        url=SQLALCHEMY_DATABASE_URL
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
