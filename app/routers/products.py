from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models import Product
from app.schemas import ProductCreate, ProductResponse
from app.database import get_db

router = APIRouter()

@router.get("/", response_model=List[ProductResponse])
def get_products(db: Session = Depends(get_db)):
    return db.query(Product).all()

@router.post("/", response_model=ProductResponse)
def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    new_product = Product(**product.dict())
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product
