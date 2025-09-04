from sqlalchemy.orm import DeclarativeBase, declared_attr

class Base(DeclarativeBase):
    __abstract__ = True

    # Esto asegura que las tablas tengan nombres en minúsculas automáticamente
    @declared_attr.directive
    def __tablename__(cls) -> str:
        return cls.__name__.lower()

    def __repr__(self) -> str:  # Representación útil para debugging
        cols = [f"{c.name}={getattr(self, c.name)!r}" for c in self.__table__.columns]
        return f"<{self.__class__.__name__} {', '.join(cols)}>"
