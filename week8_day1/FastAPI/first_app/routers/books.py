from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional

router = APIRouter(
    prefix="/books",
    tags=['Books']
)

class BoolModel(BaseModel):
    title:str
    author:str
    price:float
    in_stock:Optional[bool] = True
    
@router.post("/new")
def add_book(book:BoolModel):
    return {
        "message": f"Book added successfully. Book '{book.title}' by {book.author} added. In Stock: {book.in_stock}, Price: {book.price}"
    }