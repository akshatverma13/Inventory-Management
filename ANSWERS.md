# ANSWERS

### 1. What database and ORM did you choose and why?
I chose SQLite for simplicity and easy setup. It’s lightweight, works well for small projects or prototypes, and requires no extra setup.git i



### 2. What's wrong with this code? How would you fix it?
```python
@app.get("/search")
async def search_products(name: str):
  query = f"SELECT * FROM products WHERE name = '{name}'"
  return database.execute(query)
Problems:

SQL Injection risk: Directly using user input in query.

No async database handling: Could block server.

No result parsing: Just returns raw database cursor.

Fix:

Use parameterized queries or ORM.

Example using SQLAlchemy:

@app.get("/search")
async def search_products(name: str):
    result = await database.fetch_all(
        query="SELECT * FROM products WHERE name = :name",
        values={"name": name}
    )
    return result

3. Explain the difference: When should you use GET vs POST? Example from API

GET: Used to retrieve data, should not change server state.
Example: GET /products → fetch all products.

POST: Used to create new data on the server.
Example: POST /products → create a new product


4. If your /products endpoint is very slow with 10,000 products. List 2 possible reasons and solutions

Reason: Returning all products at once.
Solution: Implement pagination (limit and offset) so only a subset is sent at a time.

Reason: Inefficient queries or filtering.
Solution: Optimize queries, add indexes on searchable fields (like name or category).

5. Bugs found and fixed in the debug section (Part B)

No unique product ID: Old code used len(products) which can duplicate IDs.
Fix: Added next_id counter to give each product a unique ID.

Type mismatch in update stock: Old code used product_id: str but IDs were integers.
Fix: Changed to int.

Update stock loop bug: Old comparison failed because of type mismatch.
Fix: IDs now integers, comparison works correctly.

Delete product bug: Old code used products.pop(product_id) → deleted by list index, could remove wrong product.
Fix: Find product by ID and remove it safely.

No error handling when product not found: Old code returned plain message, no proper HTTP error.
Fix: Added HTTPException(status_code=404) for proper error handling.