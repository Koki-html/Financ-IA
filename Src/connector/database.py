from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import dotenv_values
from Src.models.base import Base

# Conexión a la base de datos con SQLAlchemy
def ConectDatabase():
    # Cargar configuración desde .env
    config = dotenv_values(".env")
    DBURL = config["URL"]

    # Crear el motor de conexión
    engine = create_engine(DBURL)

    # Crear las tablas en la base de datos si no existen
    Base.metadata.create_all(bind=engine)

    # Retornar el motor para usarlo en otros módulos
    return engine

# Crear una sesión para interactuar con la base de datos
engine = ConectDatabase()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)