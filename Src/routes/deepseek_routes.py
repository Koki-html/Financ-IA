from fastapi import APIRouter
from pydantic import BaseModel
from Src.connector.deepseek_conector import get_deepseek_response

router = APIRouter()
class UserMessage(BaseModel):
    user_message: str

@router.post("/deepseek/chat")
async def deepseek_chat(message: UserMessage):
    try:
        response = get_deepseek_response(message.user_message)
        return {"response": response}
    except Exception as e:
        return {"error": str(e)}