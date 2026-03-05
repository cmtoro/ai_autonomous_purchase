from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Product(BaseModel):
    id: int
    name: str
    price: float

# Temporary in-memory database for the MVP
inventory = [
    {"id": 1, "name": "Keyboard", "price": 50.0},
    {"id": 2, "name": "Mouse", "price": 25.0}
]

@app.get("/products")
def list_products():
    return inventory

@app.post("/products")
def add_product(prod: Product):
    inventory.append(prod.dict())
    return {"status": "Product added."}