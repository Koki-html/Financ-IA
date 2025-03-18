#ejemplo de query para más adelante
from Src.models.dbmodels import User, engine
from sqlalchemy import select

#conexión con la DB
conexion = engine.connect()

#Generación de query
stmt = select(User)

data = conexion.execute(stmt)

#Impresión de resultados
for row in data:
    print(row)

conexion.close()