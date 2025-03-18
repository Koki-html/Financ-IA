from Src.models.dbmodels import User, engine, initialize_db
from sqlalchemy import select

conexion = engine.connect()

initialize_db()
stmt = select(User)

data = conexion.execute(stmt)

print(data)

conexion.close()