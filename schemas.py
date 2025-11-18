from pydantic import BaseModel,Field, EmailStr
from typing import Optional

class Userschema(BaseModel):
    name: str
    email: EmailStr
    password: str = Field(..., min_length=8)
    active: Optional[bool] = True
    admin: Optional[bool] = False

    class Config:
        from_attributes = True

class LoginSchema(BaseModel):
    email: str
    password: str
