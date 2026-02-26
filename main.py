from fastapi import FastAPI

from v1.db.base import Base
from v1.db.database import engine
from v1.endpoints.router_products import router as products 
from v1.endpoints.router_register import router as user

app = FastAPI()

@app.get("/")
def read_root():
    return {"MESSAGE": "INICIO APP"}   
Base.metadata.create_all(bind=engine)
"""
Finalmente, tenemos este codigo, que se encarga de crear las tablas en la base de datos, utilizando el motor creado anteriormente. Esto es importante para que la base de datos tenga las tablas necesarias para almacenar los datos de los usuarios.
"""
app.include_router(user)
app.include_router(products)


