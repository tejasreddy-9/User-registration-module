from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.encoders import jsonable_encoder
from models import RegisterUser, LoginUser, ChangePassword, ForgetPasswordRequest, ResetPassword
from database import user_collection
from utils.password_utils import *
from auth.jwt_handler import create_jwt_token, get_current_user
from logger import logging

user_router = APIRouter()

@user_router.post("/register")
def register(user: RegisterUser):
    if user_collection.find_one({"username": user.username}):
        raise HTTPException(status_code=409, detail="User already exists")
    
    user_dict = user.dict()
    user_dict["password"] = hash_password(user.password)
    user_dict = jsonable_encoder(user_dict) 

    user_collection.insert_one(user_dict)
    logging.info(f"User registered: {user.username}")
    return {"message": "User registered successfully"}

@user_router.post("/login")
def login(user: LoginUser):
    found_user = user_collection.find_one({"username": user.username})
    if not found_user or not verify_password(user.password, found_user["password"]):
        logging.warning(f"Failed login for {user.username}")
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_jwt_token(user.username)
    logging.info(f"User logged in: {user.username}")
    return {"access_token": token}

@user_router.post("/change-password")
def change_password(payload: ChangePassword, username: str = Depends(get_current_user)):
    user = user_collection.find_one({"username": username})
    if not verify_password(payload.old_password, user["password"]):
        raise HTTPException(status_code=400, detail="Incorrect old password")

    if verify_password(payload.new_password, user["password"]):
        raise HTTPException(status_code=400, detail="Cannot reuse old password")

    user_collection.update_one(
        {"username": username},
        {"$set": {"password": hash_password(payload.new_password)}}
    )
    logging.info(f"Password changed for user: {username}")
    return {"message": "Password changed successfully"}
