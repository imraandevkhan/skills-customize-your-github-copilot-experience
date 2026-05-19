import sqlite3
from typing import Optional, List

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


db_path = "fastapi_items.db"


class Item(BaseModel):
    id: int
    name: str
    description: Optional[str] = None


app = FastAPI()


def get_db_connection():
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn


@app.on_event("startup")
def startup():
    conn = get_db_connection()
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS items (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            description TEXT
        )
        """
    )
    conn.commit()
    conn.close()


def row_to_item(row: sqlite3.Row) -> Item:
    return Item(id=row["id"], name=row["name"], description=row["description"])


@app.get("/items", response_model=List[Item])
def read_items():
    # Return all stored items
    pass


@app.get("/items/{item_id}", response_model=Item)
def read_item(item_id: int):
    # Return a single item by ID or raise HTTPException if not found
    pass


@app.post("/items", response_model=Item)
def create_item(item: Item):
    # Insert a new item into the database and return it
    pass


@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, item: Item):
    # Update an existing item by ID and return the updated item
    pass


@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    # Delete the item with the given ID or raise HTTPException if missing
    pass
