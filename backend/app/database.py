from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Conexión a MySQL en Docker (con nombre del contenedor como host)
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://user:userpassword@localhost:3306/techO"


# Crear el motor de SQLAlchemy
engine = create_engine(SQLALCHEMY_DATABASE_URL, pool_pre_ping=True)

# Crear una fábrica de sesiones
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Declarar una base para los modelos
Base = declarative_base()

# Dependencia para obtener la sesión de la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
