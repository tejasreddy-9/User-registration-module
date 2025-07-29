from pydantic import BaseModel, EmailStr, Field, validator
from typing import Optional
from datetime import date

class RegisterUser(BaseModel):
    username: EmailStr
    first_name: str
    last_name: str
    dob: date
    doj: date
    address: str
    comment: Optional[str]
    active: bool
    password: str

    @validator("username")
    def validate_email_domain(cls, value):
        allowed_domains = ["@gmail.com", "@yahoo.com", "@outlook.com"]
        if not any(value.endswith(domain) for domain in allowed_domains):
            raise ValueError("Email must be @gmail.com, @yahoo.com, or @outlook.com only")
        return value

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
