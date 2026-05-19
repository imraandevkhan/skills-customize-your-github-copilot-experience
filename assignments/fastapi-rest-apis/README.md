# 📘 Assignment: FastAPI REST APIs

## 🎯 Objective

Build a REST API with the FastAPI framework to gain hands-on experience with Python web services, Pydantic models, HTTP operations, and automatic API documentation.

## 📝 Tasks

### 🛠️ Create REST API Endpoints

#### Description
Create a FastAPI app that manages a list of items. Define routes for retrieving all items and individual items by ID.

#### Requirements
Completed program should:

- Create a `FastAPI()` application instance.
- Define `GET /items` to return a list of items.
- Define `GET /items/{item_id}` to return a single item by its ID.
- Use a Pydantic model to structure item data.
- Return JSON responses and handle missing items with an error.

### 🛠️ Add Create, Update, and Delete Operations

#### Description
Extend the API with endpoints to create, update, and delete items. Ensure the API returns appropriate responses for successful and failed operations.

#### Requirements
Completed program should:

- Define `POST /items` to create a new item from JSON request data.
- Define `PUT /items/{item_id}` to update an existing item.
- Define `DELETE /items/{item_id}` to remove an item.
- Use `HTTPException` for not-found cases and return a clear error message.
- Confirm the API documentation is available at `/docs` when the app is running.
- Example request body:
  ```json
  {
    "id": 2,
    "name": "New item",
    "description": "A short description"
  }
  ```
