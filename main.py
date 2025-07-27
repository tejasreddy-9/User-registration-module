from fastapi import FastAPI
from routes.user import user_router
from logger import setup_logger

app = FastAPI(title="User Registration Module")
setup_logger()

app.include_router(user_router, prefix="/user")