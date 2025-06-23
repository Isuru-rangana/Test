from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI(title="Choreo Sample API")

# Sample data model
class Item(BaseModel):
    id: int
    name: str
    description: Optional[str] = None

# In-memory storage
items_db = []

@app.get("/")
def read_root():
    return {"message": "Welcome to Choreo Sample API"}

@app.get("/items", response_model=List[Item])
def get_items():
    return items_db

@app.post("/items", response_model=Item)
def create_item(item: Item):
    items_db.append(item)
    return item

@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int):
    item = next((item for item in items_db if item.id == item_id), None)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item
