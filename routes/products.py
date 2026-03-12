from fastapi import APIRouter
from models import Product
from database import products_collection

router = APIRouter(prefix="/products", tags=["Products"])

@router.post("/")
def add_product(product: Product):
    products_collection.insert_one(product.dict())
    return {"msg": "Produto adicionado"}

@router.get("/")
def list_products():
    return list(products_collection.find())

@router.put("/{name}")
def update_product(name: str, product: Product):
    products_collection.update_one({"name": name}, {"$set": product.dict()})
    return {"msg": "Produto atualizado"}

@router.delete("/{name}")
def delete_product(name: str):
    products_collection.delete_one({"name": name})
    return {"msg": "Produto deletado"}
