from pydantic import BaseModel
from datetime import date, datetime
from typing import Optional

class User(BaseModel):
    #id: Optional[bytes]  # Opcional porque puede no estar presente en algunas operaciones
    run: str
    name: str
    last_name: str
    password: str
    email: str
    phone: str
    birthdate: date

class Reports(BaseModel):
    #id: Optional[bytes]
    user_id: bytes
    report: str
    creation_date: date

class Debs(BaseModel):
    #id: Optional[bytes]
    user_id: bytes
    value: float
    start_date: date
    end_date: date
    explain_debt: str

class Types(BaseModel):
    #id: Optional[bytes]
    name: str

class FinanceUser(BaseModel):
    #id: Optional[bytes]
    user_id: bytes
    value: float
    start_date: date
    explain_finance: str
    type_id: bytes

class Messages(BaseModel):
    #id: Optional[bytes]
    user_id: bytes
    message: str
    creation_date: datetime
    ia_response: bool