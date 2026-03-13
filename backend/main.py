from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # For MVP only
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/v1/health")
def health_check():
    return {"status": "online", "message": "Backend is reachable"}

class Product(BaseModel):
    id: int
    name: str
    price: float

# Temporary in-memory database for the MVP
inventory = [
    {"id": 1, "name": "Keyboard", "price": 50.0},
    {"id": 2, "name": "Mouse", "price": 25.0}
]

@app.get("/api/v1/products")
def list_products():
    return inventory

@app.post("/api/v1/products")
def add_product(prod: Product):
    inventory.append(prod.dict())
    return {"status": "Product added."}