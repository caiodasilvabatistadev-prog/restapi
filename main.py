from fastapi import FastAPI
from auth_routes import auth_router
from order_routes import order_router
from passlib.context import CryptContext
from dotenv import load_dotenv
import os

app = FastAPI()
app.include_router(auth_router)
app.include_router(order_router)

load_dotenv()

secret_key = os.getenv("SECRET_KEY")


bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")






