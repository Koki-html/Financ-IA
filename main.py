from fastapi import FastAPI
from Src.routes.deepseek_routes import router as deepseek_router

app = FastAPI()

app.include_router(deepseek_router, prefix="/api")