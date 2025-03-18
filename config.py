# Tengo que tener las variable de entorno en el .env y despues llamarles tras los = en el config.py.

from dataclasses import dataclass
import os

@dataclass
class Config:
    SQLALCHEMY_DATABASE_URI: str = ''
    SQLALCHEMY_TRACK_MODIFICATIONS: bool = False,
    OPENAI_API_KEY: str = os.getenv('OPENAI_API_KEY', '')
    OPENAI_BASE_URL: str = os.getenv('OPENAI_BASE_URL', '')

config = Config()

