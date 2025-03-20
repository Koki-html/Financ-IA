from fastapi import APIRouter
from pydantic import BaseModel
from Src.connector.deepseek_conector import get_deepseek_response

router = APIRouter()

class UserMessage(BaseModel):
    user_message: str

@router.post("/deepseek/chat")
async def deepseek_chat(payload: UserMessage):
    """
    Endpoint para interactuar con el modelo DeepSeek.
    :param payload: Mensaje enviado por el usuario.
    :return: Respuesta generada por el modelo.
    """
    try:
        response = get_deepseek_response(payload.user_message)
        return {"response": response}
    except Exception as e:
        return {"error": str(e)}