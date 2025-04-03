from sqlalchemy.orm import Session
from Src.models.dbmodels import Debts  # Modelo de SQLAlchemy para la base de datos
from Src.models.PModels import Debts as DebtsPm  # Modelo de Pydantic para validación
import uuid

def get_all_debts(db: Session):
    """Obtiene todos los registros de Debts."""
    return db.query(Debts).all()

def get_debt_by_id(db: Session, debt_id: str):
    """Obtiene un registro de Debts por su ID."""
    return db.query(Debts).filter(Debts.id == debt_id).first()

def create_debt(db: Session, debt_data: DebtsPm):
    """Crea un nuevo registro en Debts."""
    new_debt = Debts(
        id=uuid.uuid4().bytes,  # Genera un UUID en formato binario
        user_id=uuid.UUID(debt_data.user_id).bytes,  # Convierte el UUID a binario
        value=debt_data.value,
        start_date=debt_data.start_date,
        end_date=debt_data.end_date,
        explain_debt=debt_data.explain_debt
    )
    db.add(new_debt)
    db.commit()
    db.refresh(new_debt)
    return new_debt

def update_debt(db: Session, debt_id: str, debt_data: DebtsPm):
    """Actualiza un registro existente en Debts."""
    debt = db.query(Debts).filter(Debts.id == debt_id).first()
    if not debt:
        return None

    # Actualiza solo los campos proporcionados
    if debt_data.user_id:
        debt.user_id = uuid.UUID(debt_data.user_id).bytes  # Convierte a binario
    if debt_data.value:
        debt.value = debt_data.value
    if debt_data.start_date:
        debt.start_date = debt_data.start_date
    if debt_data.end_date:
        debt.end_date = debt_data.end_date
    if debt_data.explain_debt:
        debt.explain_debt = debt_data.explain_debt

    db.commit()
    db.refresh(debt)
    return debt

def delete_debt(db: Session, debt_id: str):
    """Elimina un registro de Debts por su ID."""
    debt = db.query(Debts).filter(Debts.id == debt_id).first()
    if not debt:
        return None
    db.delete(debt)
    db.commit()
    return debt