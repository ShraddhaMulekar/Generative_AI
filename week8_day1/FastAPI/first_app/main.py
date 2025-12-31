from fastapi import FastAPI
from typing import Optional
from routers import orders
from routers import users
from routers import products
from routers import books
from db import models
from db.database import engine, Base

app = FastAPI()

app.include_router(orders.router)
app.include_router(users.router)
app.include_router(products.router)
app.include_router(books.router)

Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return {"message": "Hello World"}

#greet endpoint
@app.get("/greet")
def read_greet():
    return {"message": "Hello Progression!"}