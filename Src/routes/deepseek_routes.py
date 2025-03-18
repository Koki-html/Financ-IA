from fastapi import APIRouter
from Src.connector.deepseek_conector import client

router = APIRouter()

@router.post("/deepseek/chat")
async def deepseek_chat(user_message: str):
    """
    Endpoint para interactuar con el modelo DeepSeek.
    :param user_message: Mensaje enviado por el usuario.
    :return: Respuesta generada por el modelo.
    """
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": "You are a helpful assistant"},
            {"role": "user", "content": user_message},
        ],
        stream=False
    )
    return {"response": response.choices[0].message.content}