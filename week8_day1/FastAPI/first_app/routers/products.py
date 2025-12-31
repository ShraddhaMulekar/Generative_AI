from fastapi import APIRouter
from typing import Optional

router = APIRouter(
    prefix="/products",
    tags=['Products']
)

@router.get("/products")
def get_products(
    category : Optional[str] = None,
    page: int=1
):
    return {"message": f"Products in category: {category}, page: {page}"}