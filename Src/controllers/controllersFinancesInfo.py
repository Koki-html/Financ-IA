from sqlalchemy.orm import Session
from Src.models.dbmodels import FinanceUser  # Modelo de SQLAlchemy para la base de datos
from Src.models.PModels import FinanceUserSchema  # Modelo de Pydantic para validación
import uuid

def get_all_finance_info(db: Session):
    """Obtiene todos los registros de FinanceUser."""
    return db.query(FinanceUser).all()

def get_finance_info_by_id(db: Session, finance_id: str):
    """Obtiene un registro de FinanceUser por su ID."""
    return db.query(FinanceUser).filter(FinanceUser.id == finance_id).first()

def create_finance_info(db: Session, finance_data: FinanceUserSchema):
    """Crea un nuevo registro en FinanceUser asegurando que los UUID sean válidos."""
    
    def clean_uuid(uuid_str):
        return uuid_str.replace("0x", "") if isinstance(uuid_str, str) else uuid_str.hex
    
    user_id = clean_uuid(finance_data.user_id)
    type_id = clean_uuid(finance_data.type_id)

    new_finance_info = FinanceUser(
        id=uuid.uuid4().bytes,
        user_id=uuid.UUID(user_id).bytes,
        value=finance_data.value,
        start_date=finance_data.start_date,
        explain_finance=finance_data.explain_finance,
        type_id=uuid.UUID(type_id).bytes
    )
    
    db.add(new_finance_info)
    db.commit()
    db.refresh(new_finance_info)
    
    return new_finance_info

def update_finance_info(db: Session, finance_id: str, finance_data: FinanceUserSchema):
    """Actualiza un registro existente en FinanceUser."""
    finance_info = db.query(FinanceUser).filter(FinanceUser.id == finance_id).first()
    if not finance_info:
        return None
    
    # Actualiza solo los campos proporcionados
    if finance_data.user_id:
        finance_info.user_id = uuid.UUID(finance_data.user_id).bytes  # Convierte a binario
    if finance_data.value:
        finance_info.value = finance_data.value
    if finance_data.start_date:
        finance_info.start_date = finance_data.start_date
    if finance_data.explain_finance:
        finance_info.explain_finance = finance_data.explain_finance
    if finance_data.type_id:
        finance_info.type_id = uuid.UUID(finance_data.type_id).bytes  # Convierte a binario
    
    db.commit()
    db.refresh(finance_info)
    return finance_info

def delete_finance_info(db: Session, finance_id: str):
    """Elimina un registro de FinanceUser por su ID."""
    finance_info = db.query(FinanceUser).filter(FinanceUser.id == finance_id).first()
    if not finance_info:
        return None
    db.delete(finance_info)
    db.commit()
    return finance_info