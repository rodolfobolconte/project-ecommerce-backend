from fastapi import APIRouter
from models import Cart
from database import cart_collection

router = APIRouter(prefix="/cart", tags=["Cart"])

@router.post("/")
def add_to_cart(cart: Cart):
    cart_collection.update_one(
        {"user_id": cart.user_id},
        {"$set": cart.dict()},
        upsert=True
    )
    return {"msg": "Carrinho atualizado"}

@router.get("/{user_id}")
def get_cart(user_id: str):
    return cart_collection.find_one({"user_id": user_id})
