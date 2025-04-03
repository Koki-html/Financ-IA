from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from Src.connector.database import engine
from Src.controllers.controllersFinancesInfo import (
    get_all_finance_info,
    get_finance_info_by_id,
    create_finance_info,
    update_finance_info,
    delete_finance_info
)
from Src.models.PModels import FinanceUserSchema  # Modelo de Pydantic
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

@router.get("/financeinfo", response_model=list[FinanceUserSchema])
async def read_all_finance_info(db: Session = Depends(get_db)):
    """Obtiene todos los registros de FinanceUser."""
    return get_all_finance_info(db)

@router.get("/financeinfo/{finance_id}", response_model=FinanceUserSchema)
async def read_finance_info(finance_id: str, db: Session = Depends(get_db)):
    """Obtiene un registro de FinanceUser por su ID."""
    finance_info = get_finance_info_by_id(db, finance_id)
    if not finance_info:
        raise HTTPException(status_code=404, detail="FinanceInfo no encontrado")
    return finance_info

@router.post("/financeinfo", response_model=FinanceUserSchema)
async def create_finance_info_endpoint(finance_data: FinanceUserSchema, db: Session = Depends(get_db)):
    """Crea un nuevo registro en FinanceUser."""
    return create_finance_info(db, finance_data)

@router.put("/financeinfo/{finance_id}", response_model=FinanceUserSchema)
async def update_finance_info_endpoint(finance_id: str, finance_data: FinanceUserSchema, db: Session = Depends(get_db)):
    """Actualiza un registro existente en FinanceUser."""
    updated_finance_info = update_finance_info(db, finance_id, finance_data)
    if not updated_finance_info:
        raise HTTPException(status_code=404, detail="FinanceInfo no encontrado")
    return updated_finance_info

@router.delete("/financeinfo/{finance_id}")
async def delete_finance_info_endpoint(finance_id: str, db: Session = Depends(get_db)):
    """Elimina un registro de FinanceUser por su ID."""
    deleted_finance_info = delete_finance_info(db, finance_id)
    if not deleted_finance_info:
        raise HTTPException(status_code=404, detail="FinanceInfo no encontrado")
    return {"detail": "FinanceInfo eliminado correctamente"}

