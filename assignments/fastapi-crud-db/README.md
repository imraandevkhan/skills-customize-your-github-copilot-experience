# 📘 Assignment: FastAPI CRUD with Database Persistence

## 🎯 Objective

Build a FastAPI application that stores data in SQLite and supports full CRUD operations. Learn how to connect web endpoints to a persistent backend and return structured JSON responses.

## 📝 Tasks

### 🛠️ Set Up the FastAPI App and Database

#### Description
Create a FastAPI app with a SQLite database backend. Define the item model and database initialization logic so the app can store data persistently.

#### Requirements
Completed program should:

- Create a `FastAPI()` application instance.
- Define a Pydantic model for an item with `id`, `name`, and optional `description`.
- Initialize a SQLite database table when the app starts.
- Use the database to persist items between requests.

### 🛠️ Implement CRUD Endpoints

#### Description
Add API endpoints for creating, reading, updating, and deleting items. Use HTTP status codes and error handling for missing records.

#### Requirements
Completed program should:

- Define `GET /items` to retrieve all items from the database.
- Define `GET /items/{item_id}` to retrieve a specific item by ID.
- Define `POST /items` to create a new item from JSON request data.
- Define `PUT /items/{item_id}` to update an existing item.
- Define `DELETE /items/{item_id}` to delete an item.
- Use `HTTPException` for not-found cases and return a clear error message.
- Example request body:
  ```json
  {
    "id": 2,
    "name": "New item",
    "description": "A short description"
  }
  ```
