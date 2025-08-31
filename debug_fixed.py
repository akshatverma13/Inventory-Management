from fastapi import FastAPI, HTTPException
from typing import List, Dict, Any
from pydantic import BaseModel

app = FastAPI()

class Product(BaseModel):
    name: str
    price: float
    stock: int = 0

class StockUpdate(BaseModel):
    quantity: int

products: List[Dict[str, Any]] = []
next_id = 0  # Track next available ID

@app.get("/products", response_model=List[Dict[str, Any]])
def get_products() -> List[Dict[str, Any]]:
    return products

@app.post("/products", response_model=Dict[str, Any])
def create_product(product: Product):
    global next_id
    product_data = product.dict()
    product_data["id"] = next_id
    products.append(product_data)
    next_id += 1  # Increment for next product
    return {"message": "Created", "id": product_data["id"]}

@app.put("/products/{product_id}/stock")
def update_stock(product_id: int, stock: StockUpdate):
    for product in products:
        if product["id"] == product_id:
            product["stock"] = stock.quantity
            return {"message": "Updated"}
    raise HTTPException(status_code=404, detail="Product not found")

@app.delete("/products/{product_id}")
def delete_product(product_id: int):
    for i, product in enumerate(products):
        if product["id"] == product_id:
            products.pop(i)
            return {"message": "Deleted"}
    raise HTTPException(status_code=404, detail="Product not found")