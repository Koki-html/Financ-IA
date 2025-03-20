from fastapi import FastAPI
#from Src.routes.deepseek_routes import router as deepseek_router
from Src.routes.users_routes import router as database_router

app = FastAPI()

#app.include_router(deepseek_router, prefix="/api")
app.include_router(database_router, prefix="/api")