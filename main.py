from fastapi import FastAPI
from routes import users, products, cart, orders

app = FastAPI(title="E-commerce API")

app.include_router(users.router)
app.include_router(products.router)
app.include_router(cart.router)
app.include_router(orders.router)
