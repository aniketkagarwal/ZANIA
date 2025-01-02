from pydantic import BaseModel
from typing import List, Dict

class ProductCreate(BaseModel):
    name: str
    description: str
    price: float
    stock: int

class ProductResponse(ProductCreate):
    id: int

    class Config:
        orm_mode = True

class OrderCreate(BaseModel):
    products: List[Dict[str, int]]

class OrderResponse(BaseModel):
    id: int
    total_price: float
    status: str

    class Config:
        orm_mode = True
