from pydantic import BaseModel, UUID4
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

class Debts(BaseModel):
    #id: Optional[bytes]
    user_id: bytes
    value: float
    start_date: date
    end_date: date
    explain_debt: str

class Types(BaseModel):
    #id: Optional[bytes]
    name: str

class FinanceUserSchema(BaseModel):
    user_id: UUID4  # Usar UUID4 para validación automática
    value: float
    start_date: date
    explain_finance: str
    type_id: UUID4  # Usar UUID4 para validación automática

    @classmethod
    def validate_uuid(cls, uuid_str: str) -> str:
        """ Elimina el prefijo '0x' si está presente. """
        return uuid_str.replace("0x", "")

    def __init__(self, **data):
        if "user_id" in data:
            data["user_id"] = self.validate_uuid(data["user_id"])
        if "type_id" in data:
            data["type_id"] = self.validate_uuid(data["type_id"])
        super().__init__(**data)

class Messages(BaseModel):
    #id: Optional[bytes]
    user_id: bytes
    message: str
    creation_date: datetime
    ia_response: bool

#class for Updates

class UserUpdate(BaseModel):
    id: Optional[bytes] = None
    run: Optional[str] = None
    name: Optional[str] = None
    last_name: Optional[str] = None
    password: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    birthdate: Optional[date] = None