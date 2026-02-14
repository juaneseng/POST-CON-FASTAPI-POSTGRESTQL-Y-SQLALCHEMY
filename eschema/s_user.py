from pydantic import BaseModel , EmailStr

class sUser(BaseModel):
    email: EmailStr
    password: str