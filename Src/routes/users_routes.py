from fastapi import APIRouter, HTTPException
from Src.controllers.users import get_users, create_users
from Src.models.PModels import User as UserCreate

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
    