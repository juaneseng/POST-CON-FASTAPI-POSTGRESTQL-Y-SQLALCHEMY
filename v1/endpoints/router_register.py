import bcrypt

from v1.db.database import get_db
from v1.schema.login import LoginRequest
from v1.schema.register_schema import sUser
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session


from v1.models.register_model import mUser

router = APIRouter(prefix="/users")

@router.post("/")
def create_user(user: sUser, db: Session = Depends(get_db)):
    data = user.model_dump()
    hashed = bcrypt.hashpw(data["password"].encode("utf-8"), bcrypt.gensalt())
    data["password"] = hashed.decode("utf-8")
    db_user = mUser(**data)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@router.post("/join")
def join_user(user: LoginRequest, db: Session = Depends(get_db)):
    found = (
        db.query(mUser)
        .filter(mUser.email == user.email)
        .first()
    )

    if not found or not bcrypt.checkpw(user.password.encode("utf-8"), found.password.encode("utf-8")):
        raise HTTPException(status_code=401, detail="credenciales invalidas")

    return {"Mensaje": "Sesion correctamente iniciada"}