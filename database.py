from sqlalchemy import create_engine
from dotenv import dotenv_values

# Conexión a la base de datos con SQLAlchemy e importando variables de .env
config = dotenv_values(".env")
DBURL = config["URL"]
engine = create_engine(DBURL)
