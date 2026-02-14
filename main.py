from fastapi import FastAPI
from model import Base
from routers.r_user import router as user_router
from db import engine

Base.metadata.create_all(bind=engine)
    

app = FastAPI()
app.include_router(user_router)

