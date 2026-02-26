from pydantic import BaseModel, EmailStr


class sUser(BaseModel):
    name: str
    last_name: str
    email: EmailStr
    password: str

