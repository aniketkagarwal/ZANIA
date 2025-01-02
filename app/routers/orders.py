from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.models import Product, Order
from app.schemas import OrderCreate, OrderResponse
from app.database import get_db
from app.exceptions import insufficient_stock_exception

router = APIRouter()

@router.post("/", response_model=OrderResponse)
def place_order(order: OrderCreate, db: Session = Depends(get_db)):
    total_price = 0
    for item in order.products:
        product = db.query(Product).filter(Product.id == item["id"]).first()
        if not product or product.stock < item["quantity"]:
            insufficient_stock_exception(item["id"])
        product.stock -= item["quantity"]
        db.commit()
        total_price += product.price * item["quantity"]

    new_order = Order(total_price=total_price, status="completed")
    db.add(new_order)
    db.commit()
    db.refresh(new_order)
    return new_order
