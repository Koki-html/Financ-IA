#Este archivo es usado para importar todos los modulos necesarios para la conexión a la DB
from Src.connector.database import engine
from Src.models import dbmodels
from controllers import ReadUsers
from Src.controllers.users import CreateUser
from Src.connector.database import ConectDatabase
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

ConectDatabase()