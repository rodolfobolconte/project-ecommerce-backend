from pymongo import MongoClient

# Conexão com MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["ecommerce_db"]

# Coleções
users_collection = db["users"]
products_collection = db["products"]
cart_collection = db["carts"]
orders_collection = db["orders"]
