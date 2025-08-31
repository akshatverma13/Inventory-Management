# ANSWERS

1. What database and ORM did you choose and why?

I picked SQLite because it’s very simple, light, and doesn’t need any setup. It’s great for small projects or practice.
I used SQLAlchemy because it lets me use Python code instead of writing SQL. This makes things safer and easier to understand.

2. What's wrong with this code? How would you fix it?
```python
@app.get("/search")
async def search_products(name: str):
  query = f"SELECT * FROM products WHERE name = '{name}'"
  return database.execute(query)
  
Problems:

- It says async but doesn’t actually use async database calls.
- No database connection is defined, so it won’t even run.
- It directly puts user input into SQL — that’s a SQL injection risk.
- The database object itself is not set up.

Fix:

- Removed async
- No SQL injection problem
- Doesn’t need database setup
- Works fine with the in-memory list

Example using SQLAlchemy:

@app.get("/search")
def search_products(name: str):
    return [p for p in products if p.get("name") == name]


3. Difference between GET and POST (with API example)

GET:
1.Used to get data from the server.
2.It should not change anything on the server.
Example: GET /products → Returns a list of all products.

POST:

1.Used to send data to the server to create something new.
Example: POST /products → Creates a new product in the database.

4. Why /products might be slow with 10,000 items (and how to fix it)

Reason 1: Trying to return all products at once.
Solution: Use pagination (e.g., limit and offset) to load a few items at a time instead of everything.

Reason 2: Slow database queries.
Solution: Optimize your queries and add indexes to fields like name or category to speed up searching and filtering.

5. Bugs found and fixed in the debug section (Part B)

Type Fix: Changed product_id from a string to an integer in update_stock to match how IDs are stored.

Logic Fix: Moved the "not found" response outside the loop in update_stock so it works properly.

Deletion Fix: Updated delete_product to find the product by its actual ID instead of using its position in a list.

Error Handling: Added proper error messages using HTTPException with a 404 status when a product isn’t found.

Security Fix: Removed unsafe SQL code and used a safe list search to prevent SQL injection risks.

Code Cleanup: Improved code structure and indentation to make it easier to read and maintain.