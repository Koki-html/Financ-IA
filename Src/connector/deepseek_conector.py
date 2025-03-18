from openai import OpenAI
import os

api_key = os.getenv("API_KEY")
base_url = os.getenv("BASE_URL")

client = OpenAI(api_key=api_key, base_url=base_url)

def get_deepseek_response(user_message: str) -> str:
    """
    Función para interactuar con el modelo DeepSeek.
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
    return response.choices[0].message.content