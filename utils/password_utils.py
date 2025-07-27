from passlib.context import CryptContext
import re
from fastapi import HTTPException

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str):
    if not validate_password_policy(password):
        raise HTTPException(status_code=400, detail="Password policy not met")
    return pwd_context.hash(password)

def verify_password(plain: str, hashed: str):
    return pwd_context.verify(plain, hashed)

def validate_password_policy(password: str):
    if len(password) < 8 or len(password) > 20:
        return False
    if not re.search(r"[A-Z]", password): return False
    if not re.search(r"[a-z]", password): return False
    if not re.search(r"[0-9]", password): return False
    if not re.search(r"[!@#$%^&*]", password): return False
    return True