from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException
from db import get_db
from models.m_user import mUser
from eschema.s_user import sUser

router = APIRouter(
    prefix="/users",
)


@router.post("/", response_model=sUser)
def create_user(user: sUser, db: Session = Depends(get_db)):
    db_user = mUser(**user.dict())
    db.add(db_user)

    db.commit()
    db.refresh(db_user)
    return db_user