from sqlalchemy import create_engine
import os

# Conexión a la base de datos con SQLAlchemy e importando variables de .env
DBURL = os.getenv("URL")
engine = create_engine(DBURL)