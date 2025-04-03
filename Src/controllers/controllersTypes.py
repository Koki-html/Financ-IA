from sqlalchemy.orm import Session
from Src.models.dbmodels import Types
from Src.models.PModels import Types as TypesSchema
import uuid

def get_all_types(db: Session):
    """Obtiene todos los registros de Types."""
    return db.query(Types).all()

def get_type_by_id(db: Session, type_id: str):
    """Obtiene un registro de Types por su ID."""
    return db.query(Types).filter(Types.id == type_id).first()

def create_type(db: Session, type_data: TypesSchema):
    """Crea un nuevo registro en Types."""
    new_type = Types(
        id=uuid.uuid4().bytes,
        name=type_data.name
    )
    db.add(new_type)
    db.commit()
    db.refresh(new_type)
    return new_type

def update_type(db: Session, type_id: str, type_data: TypesSchema):
    """Actualiza un registro existente en Types."""
    type_record = db.query(Types).filter(Types.id == type_id).first()
    if not type_record:
        return None
    type_record.name = type_data.name
    db.commit()
    db.refresh(type_record)
    return type_record

def delete_type(db: Session, type_id: str):
    """Elimina un registro de Types por su ID."""
    type_record = db.query(Types).filter(Types.id == type_id).first()
    if not type_record:
        return None
    db.delete(type_record)
    db.commit()
    return type_record