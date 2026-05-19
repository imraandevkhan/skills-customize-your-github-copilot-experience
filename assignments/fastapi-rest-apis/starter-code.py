from typing import Dict, List, Optional

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


class Item(BaseModel):
    id: int
    name: str
    description: Optional[str] = None


app = FastAPI()

items: Dict[int, Item] = {
    1: Item(id=1, name="Example item", description="A sample item.")
}


@app.get("/items", response_model=List[Item])
def read_items():
    # Return all items in the API
    pass


@app.get("/items/{item_id}", response_model=Item)
def read_item(item_id: int):
    # Return a single item by ID or raise HTTPException if not found
    pass


@app.post("/items", response_model=Item)
def create_item(item: Item):
    # Add a new item to the list and return it
    pass


@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, item: Item):
    # Update an existing item by ID and return the updated item
    pass


@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    # Delete the item with the given ID or raise HTTPException if missing
    pass
