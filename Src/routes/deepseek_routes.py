from fastapi import APIRouter
from Src.connector.deepseek_conector import get_deepseek_response

router = APIRouter()

@router.post("/deepseek/chat")
async def deepseek_chat(user_message: str):
    """
    Endpoint para interactuar con el modelo DeepSeek.
    :param user_message: Mensaje enviado por el usuario.
    :return: Respuesta generada por el modelo.
    """
    try:
        response = get_deepseek_response(user_message)
        return {"response": response}
    except Exception as e:
        return {"error": str(e)}