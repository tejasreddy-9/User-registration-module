from passlib.context import CryptContext
import re
from fastapi import HTTPException

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

weak_passwords = {
    "123456", "password", "12345678", "qwerty", "abc123", "password1", "111111", "letmein", "123123", "admin"
}

def hash_password(password: str):
    if is_weak_password_gpt_agent(password):
        raise HTTPException(status_code=400, detail="Password too weak or common. Please choose a stronger password.")
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


def is_weak_password_gpt_agent(password: str) -> bool:
    # Simulate GPT-agent logic
    lowered = password.lower()
    
    # Check dictionary-based common passwords
    if lowered in weak_passwords:
        return True
    
    # Check if it’s too simple
    if lowered.isalpha() or lowered.isdigit():
        return True

    # Check length and symbol mix again
    if len(password) < 8 or not validate_password_policy(password):
        return True

    return False
