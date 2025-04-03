from fastapi import FastAPI
from Src.routes.deepseek_routes import router as deepseek_router
from Src.routes.users_routes import router as database_router
from Src.routes.finance_Info_routes import router as finance_info_router
from Src.routes.types_routes import router as types_router
from Src.routes.debts_routes import router as debts_router


app = FastAPI()

app.include_router(deepseek_router, prefix="/api")
app.include_router(database_router, prefix="/api")
app.include_router(finance_info_router, prefix="/api")
app.include_router(types_router, prefix="/api")
app.include_router(debts_router, prefix="/api")