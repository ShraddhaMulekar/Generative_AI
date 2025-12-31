from fastapi import FastAPI
from typing import Optional

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World"}

#greet endpoint
@app.get("/greet")
def read_greet():
    return {"message": "Hello Progression!"}

#parameter
@app.get("/user/{username}")
def get_user(username:str):
    return {"message": f"User profile for, {username}!"}

@app.get("/user/{username}/post/{post_id}")
def get_post(username:str, post_id:int):
    return {"message": f"Post {post_id} for user {username}!"}

#query parameter
@app.get("/products")
def get_products(
    category : Optional[str] = None,
    page: int=1
):
    return {"message": f"Products in category: {category}, page: {page}"}


#path and query parameters
@app.get("/orders/{order_id}/items/{item_id}")
def get_order_item(
    order_id: int,
    item_id: int,
    delivered: bool = False
):
    return {
        "message": f"Order {order_id}, Item {item_id}, Delivered: {delivered}"
    }

#new endpoint
@app.get("/orders/{order_id}")
def get_order(
    order_id: int,
    status: Optional[str] = None
):
    return {
        "message": f"Order {order_id}, Status: {status}"
    }