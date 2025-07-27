from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import date

class RegisterUser(BaseModel):
    username: str
    first_name: str
    last_name: str
    dob: date
    doj: date
    address: str
    comment: Optional[str]
    active: bool
    password: str

class LoginUser(BaseModel):
    username: str
    password: str

class ChangePassword(BaseModel):
    old_password: str
    new_password: str

class ForgetPasswordRequest(BaseModel):
    username: str

class ResetPassword(BaseModel):
    token: str
    new_password: str
