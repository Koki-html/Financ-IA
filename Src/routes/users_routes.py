from fastapi import APIRouter, HTTPException
from Src.controllers.users import get_users, create_users
from Src.models.PModels import User as UserCreate
from Src.models.PModels import UserUpdate
from Src.controllers.users import update_user

router = APIRouter()

@router.get("/database/readusers")
async def get_all_users():

    try:
        users = get_users()
        return {"users": users}
    except Exception as e:
        return {"error": str(e)}
    
@router.post("/database/createusers")
async def create_users_endpoint(user: UserCreate):

    try:
        new_user = create_users(user)
        return {"message": "create_users", "user": new_user}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.put("/database/updateuser/{user_id}")
async def update_user_endpoint(user_id: str, user_data: UserUpdate):

    try:
        # Eliminar el prefijo "0x" si está presente
        if user_id.startswith("0x"):
            user_id = user_id.lstrip("0x")

        try:
            user_id_bytes = bytes.fromhex(user_id)
        except ValueError:
            raise HTTPException(status_code=400, detail="El ID proporcionado no es un valor hexadecimal válido")

        print(f"ID convertido a bytes: {user_id_bytes.hex()}")  # Agregar registro de depuración

        # Llamar a la función de actualización
        updated_user = update_user(user_id_bytes, user_data)
        return {"message": "Usuario actualizado exitosamente", "user": updated_user}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))