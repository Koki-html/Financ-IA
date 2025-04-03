from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from Src.connector.database import engine
from Src.controllers.controllersTypes import (
    get_all_types,
    get_type_by_id,
    create_type,
    update_type,
    delete_type
)
from Src.models.PModels import Types as TypesSchema
from Src.models.dbmodels import Base

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

@router.get("/types", response_model=list[TypesSchema])
async def read_all_types(db: Session = Depends(get_db)):
    """Obtiene todos los registros de Types."""
    return get_all_types(db)

@router.get("/types/{type_id}", response_model=TypesSchema)
async def read_type(type_id: str, db: Session = Depends(get_db)):
    """Obtiene un registro de Types por su ID."""
    type_record = get_type_by_id(db, type_id)
    if not type_record:
        raise HTTPException(status_code=404, detail="Type no encontrado")
    return type_record

@router.post("/types", response_model=TypesSchema)
async def create_type_endpoint(type_data: TypesSchema, db: Session = Depends(get_db)):
    """Crea un nuevo registro en Types."""
    return create_type(db, type_data)

@router.put("/types/{type_id}", response_model=TypesSchema)
async def update_type_endpoint(type_id: str, type_data: TypesSchema, db: Session = Depends(get_db)):
    """Actualiza un registro existente en Types."""
    updated_type = update_type(db, type_id, type_data)
    if not updated_type:
        raise HTTPException(status_code=404, detail="Type no encontrado")
    return updated_type

@router.delete("/types/{type_id}")
async def delete_type_endpoint(type_id: str, db: Session = Depends(get_db)):
    """Elimina un registro de Types por su ID."""
    deleted_type = delete_type(db, type_id)
    if not deleted_type:
        raise HTTPException(status_code=404, detail="Type no encontrado")
    return {"detail": "Type eliminado correctamente"}