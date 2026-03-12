from pydantic import BaseModel
from typing import List, Optional

class User(BaseModel):
    id: Optional[str]
    name: str
    email: str
    password: str

class Product(BaseModel):
    id: Optional[str]
    name: str
    description: str
    price: float

class CartItem(BaseModel):
    product_id: str
    quantity: int

class Cart(BaseModel):
    user_id: str
    items: List[CartItem]

class Order(BaseModel):
    user_id: str
    items: List[CartItem]
    total: float
