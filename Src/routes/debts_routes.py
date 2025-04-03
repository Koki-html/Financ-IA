from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from Src.connector.database import engine
from Src.controllers.controllersDebts import (
    get_all_debts,
    get_debt_by_id,
    create_debt,
    update_debt,
    delete_debt
)
from Src.models.PModels import Debts  # Modelo de Pydantic
from Src.models.dbmodels import Base  # Base para crear tablas

# Crear las tablas si no existen
Base.metadata.create_all(bind=engine)

router = APIRouter()

# Dependencia para obtener la sesión de la base de datos
def get_db():
    db = Session(bind=engine)
    try:
        yield db
    finally:
        db.close()

@router.get("/debts", response_model=list[Debts])
async def read_all_debts(db: Session = Depends(get_db)):
    """Obtiene todos los registros de Debts."""
    return get_all_debts(db)

@router.get("/debts/{debt_id}", response_model=Debts)
async def read_debt(debt_id: str, db: Session = Depends(get_db)):
    """Obtiene un registro de Debts por su ID."""
    debt = get_debt_by_id(db, debt_id)
    if not debt:
        raise HTTPException(status_code=404, detail="Debt no encontrado")
    return debt

@router.post("/debts", response_model=Debts)
async def create_debt_endpoint(debt_data: Debts, db: Session = Depends(get_db)):
    """Crea un nuevo registro en Debts."""
    return create_debt(db, debt_data)

@router.put("/debts/{debt_id}", response_model=Debts)
async def update_debt_endpoint(debt_id: str, debt_data: Debts, db: Session = Depends(get_db)):
    """Actualiza un registro existente en Debts."""
    updated_debt = update_debt(db, debt_id, debt_data)
    if not updated_debt:
        raise HTTPException(status_code=404, detail="Debt no encontrado")
    return updated_debt

@router.delete("/debts/{debt_id}")
async def delete_debt_endpoint(debt_id: str, db: Session = Depends(get_db)):
    """Elimina un registro de Debts por su ID."""
    deleted_debt = delete_debt(db, debt_id)
    if not deleted_debt:
        raise HTTPException(status_code=404, detail="Debt no encontrado")
    return {"detail": "Debt eliminado correctamente"}