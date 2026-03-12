from fastapi import APIRouter
from models import User
from database import users_collection

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/")
def create_user(user: User):
    users_collection.insert_one(user.dict())
    return {"msg": "Usuário criado com sucesso"}

@router.get("/{email}")
def get_user(email: str):
    user = users_collection.find_one({"email": email})
    return user

@router.put("/{email}")
def update_user(email: str, user: User):
    users_collection.update_one({"email": email}, {"$set": user.dict()})
    return {"msg": "Usuário atualizado"}

@router.delete("/{email}")
def delete_user(email: str):
    users_collection.delete_one({"email": email})
    return {"msg": "Usuário deletado"}
