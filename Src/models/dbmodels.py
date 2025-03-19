from connector.database import engine
from sqlalchemy import String, Integer, BINARY, Boolean, Date, Double
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import mapped_column

class Base(DeclarativeBase):
    pass

# Definición de las tablas de la base de datos

class User(Base):

    __tablename__ = 'users'

    id = mapped_column(BINARY, primary_key=True)
    run = mapped_column(String)
    name = mapped_column(String)
    last_name = mapped_column(String)
    password = mapped_column(String)
    email = mapped_column(String)
    phone = mapped_column(String)
    birthdate = mapped_column(Date)
        
class Reports(Base):
    __tablename__ = 'reports'
    id = mapped_column(BINARY, primary_key=True)
    user_id = mapped_column(BINARY)
    report = mapped_column(String)
    creation_date = mapped_column(Date)

class debs(Base):
    __tablename__ = 'debs'
    id = mapped_column(BINARY, primary_key=True)
    user_id = mapped_column(BINARY)
    value = mapped_column(Double)
    start_date = mapped_column(Date)
    end_date = mapped_column(Date)
    explain_debt = mapped_column(String)

class types(Base):
    __tablename__ = 'type'
    id = mapped_column(BINARY, primary_key=True)
    name = mapped_column(String)

class finance_user(Base):
    __tablename__ = 'finance_user'
    id = mapped_column(BINARY, primary_key=True)
    user_id = mapped_column(BINARY)
    value = mapped_column(Double)
    start_date = mapped_column(Date)
    explain_finance = mapped_column(String)
    type_id = mapped_column(BINARY)

class messages:
    __tablename__ = 'messages'
    id = mapped_column(BINARY, primary_key=True)
    user_id = mapped_column(BINARY)
    message = mapped_column(String)
    creation_date = mapped_column(Date)
    ia_response = mapped_column(Boolean)
