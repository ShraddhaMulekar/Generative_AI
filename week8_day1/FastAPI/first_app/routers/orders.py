from fastapi import APIRouter
from typing import Optional
from pydantic import BaseModel

router = APIRouter(
    prefix="/orders",
    tags=["orders"]
)

@router.get('/{order_id}/items/{item_id}')
def get_order_item(
    order_id: int,
    item_id: int,
    delivered: bool = False
):
    return {
        "message": f"Order {order_id}, Item {item_id}, Delivered: {delivered}"
    }

@router.get("/{order_id}")
def get_order(order_id: int, total : float, coupon: Optional[str] = None):
    if coupon:
        final_price = total * 0.9  # Apply 10% discount
    else:
        final_price = total
    return {
        "order_id": order_id,
        "total": total,
        "discount_applied": bool(coupon),
        "final_price" : final_price
    }

class OrderModel(BaseModel):
    order_id: int
    item_name: str
    quantity: int
    price_per_item: float
    coupon_code: Optional[str] = None

@router.post("/create")
def create_order(order: OrderModel):
    total=order.quantity * order.price_per_item
    return{
        "message": f"Order {order.order_id} for {order.quantity} x {order.item_name} created. Total: {total}. Coupon applied: {order.coupon_code is not None}"
    }

@router.put('/{order_id}')
def update_order(
        order_id:int, 
        confirmed:Optional[bool]=False, 
        order: OrderModel=None
    ):
    total = order.quantity * order.price_per_item
    return {
        "message": f"Order {order_id} updated. Confirmed: {confirmed}. New total: {total}"
    }