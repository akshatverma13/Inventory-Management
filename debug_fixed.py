from fastapi import FastAPI, HTTPException
from typing import List

app = FastAPI()
products = []

@app.get("/products")
def get_products() -> List:
    return products

@app.post("/products")
def create_product(product: dict):
    product["id"] = len(products)
    products.append(product)
    return {"message": "Created"}

@app.put("/products/{product_id}/stock")
def update_stock(product_id: int, quantity: int):
    for product in products:
        if product["id"] == product_id:
            product["stock"] = quantity
            return {"message": "Updated"}
    
    raise HTTPException(status_code=404, detail="Product not found")

@app.delete("/products/{product_id}")
def delete_product(product_id: int):
    for i, product in enumerate(products):
        if product["id"] == product_id:
            products.pop(i)
            return {"message": "Deleted"}
    
    raise HTTPException(status_code=404, detail="Product not found")

# Safe search implementation without SQL injection vulnerability
@app.get("/search")
def search_products(name: str):
    results = [product for product in products if product.get("name") == name]
    return results