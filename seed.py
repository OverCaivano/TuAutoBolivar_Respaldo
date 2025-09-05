from config.cnx import SessionLocal
from users.model import User
from tasks.model import Auto

# Datos de prueba
USERS_SEED = [
    {"name": "Carlos Perez", "email": "carlos@example.com", "hashed_password": "1234"},
    {"name": "Maria Gomez", "email": "maria@example.com", "hashed_password": "1234"},
]

AUTOS_SEED = [
    {"marca": "Toyota", "modelo": "Corolla", "anio": 2019, "precio": 15000, "descripcion": "Sedán en buen estado", "owner_id": 1},
    {"marca": "Ford", "modelo": "Fiesta", "anio": 2017, "precio": 9500, "descripcion": "Económico y confiable", "owner_id": 2},
]


def seed():
    db = SessionLocal()
    try:
        # Insertar usuarios
        for u in USERS_SEED:
            exists = db.query(User).filter(User.email == u["email"]).first()
            if not exists:
                user = User(**u)
                db.add(user)
        db.commit()

        # Insertar autos
        for a in AUTOS_SEED:
            exists = db.query(Auto).filter(Auto.marca == a["marca"], Auto.modelo == a["modelo"], Auto.anio == a["anio"]).first()
            if not exists:
                auto = Auto(**a)
                db.add(auto)
        db.commit()

    finally:
        db.close()


if __name__ == "__main__":
    seed()
    print("✅ Datos de prueba insertados correctamente")
