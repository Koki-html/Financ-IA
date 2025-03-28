import uuid
from Src.models.base import Base
from sqlalchemy import String, BINARY, Boolean, Date, Double, DateTime
from sqlalchemy.orm import mapped_column

# Definición de las tablas de la base de datos
class User(Base):
    __tablename__ = 'users'

    id = mapped_column(BINARY(16), primary_key=True)
    run = mapped_column(String(50))
    name = mapped_column(String(100))
    last_name = mapped_column(String(100))
    password = mapped_column(String(255))
    email = mapped_column(String(255))
    phone = mapped_column(String(20))
    birthdate = mapped_column(Date)

class Reports(Base):
    __tablename__ = 'reports'
    id = mapped_column(BINARY, primary_key=True)
    user_id = mapped_column(BINARY)
    report = mapped_column(String)
    creation_date = mapped_column(Date)

class Debs(Base):
    __tablename__ = 'debs'
    id = mapped_column(BINARY, primary_key=True)
    user_id = mapped_column(BINARY)
    value = mapped_column(Double)
    start_date = mapped_column(Date)
    end_date = mapped_column(Date)
    explain_debt = mapped_column(String(255))

class Types(Base):
    __tablename__ = 'type'
    id = mapped_column(BINARY, primary_key=True)
    name = mapped_column(String)

class FinanceUser(Base):
    __tablename__ = 'finance_user'
    id = mapped_column(BINARY, primary_key=True)
    user_id = mapped_column(BINARY)
    value = mapped_column(Double)
    start_date = mapped_column(Date)
    explain_finance = mapped_column(String)
    type_id = mapped_column(BINARY)

class Messages(Base):
    __tablename__ = 'messages'
    id = mapped_column(BINARY, primary_key=True)
    user_id = mapped_column(BINARY)
    message = mapped_column(String)
    creation_date = mapped_column(DateTime)
    ia_response = mapped_column(Boolean)
