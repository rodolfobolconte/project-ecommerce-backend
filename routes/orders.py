from fastapi import APIRouter
from models import Order
from database import orders_collection, cart_collection, products_collection

router = APIRouter(prefix="/orders", tags=["Orders"])

@router.post("/{user_id}")
def checkout(user_id: str):
    cart = cart_collection.find_one({"user_id": user_id})
    if not cart:
        return {"msg": "Carrinho vazio"}

    total = 0
    for item in cart["items"]:
        product = products_collection.find_one({"id": item["product_id"]})
        total += product["price"] * item["quantity"]

    order = {
        "user_id": user_id,
        "items": cart["items"],
        "total": total
    }
    orders_collection.insert_one(order)
    cart_collection.delete_one({"user_id": user_id})

    return {"msg": "Compra realizada com sucesso", "order": order}
