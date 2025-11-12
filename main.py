from fastapi import FastAPI


app = FastAPI()

from auth_routes import auth_routes
from order_routes import order_routes


app.include_router(auth_routes)
app.include_router(order_routes)




#run the program with command
#on terminal : uvicorn main:app --reload

