from fastapi import FastAPI
from db.database import Base, engine
from db import models
from router import blog

Base.metadata.create_all(bind=engine)
app = FastAPI()

app.include_router(blog.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Blog Application"}