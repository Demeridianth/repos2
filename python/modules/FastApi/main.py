from enum import Enum

from pydantic import BaseModel

from fastapi import FastAPI, HTTPException

# # You can give your API a title and add additional metadata such as a description, version number, etc.
# # The description also supports markdown formatting.
# app = FastAPI(
#     title="Arjan's Handyman Emporium",
#     description="Arjan does not only code but also helps you fix things. **See what's in stock!**",
#     version="0.1.0",
# )

# # Docstrings of classes will be reflected in the API documentation in the 'Schemas' section
# class Category(Enum):
#     """Category of an item"""

#     TOOLS = "tools"
#     CONSUMABLES = "consumables"


# # You can add metadata to attributes using the Field class.
# # This information will also be shown in the auto-generated documentation.
# class Item(BaseModel):
#     """Representation of an item in the system."""

#     name: str = Field(description="Name of the item.")
#     price: float = Field(description="Price of the item in Euro.")
#     count: int = Field(description="Amount of instances of this item in stock.")
#     id: int = Field(description="Unique integer that specifies this item.")
#     category: Category = Field(description="Category this item belongs to.")


app = FastAPI()


class Category(Enum):
    TOOLS = "tools"
    CONSUMABLES = "consumables"


class Item(BaseModel):
    name: str
    price: float
    count: int
    id: int
    category: Category


items = {
    0: Item(name="Hammer", price=9.99, count=20, id=0, category=Category.TOOLS),
    1: Item(name="Pliers", price=5.99, count=20, id=1, category=Category.TOOLS),
    2: Item(name="Nails", price=1.99, count=100, id=2, category=Category.CONSUMABLES),
}


@app.get("/")
def index() -> dict[str, dict[int, Item]]:

    return {"items": items}


@app.get("/items/{item_id}")
def query_item_by_id(item_id: int) -> Item:

    if item_id not in items:
        HTTPException(status_code=404, detail=f"Item with {item_id=} does not exist.")

    return items[item_id]


Selection = dict[
    str, str | int | float | Category | None
]  # dictionary containing the user's query arguments


@app.get("/items/")
def query_item_by_parameters(
    name: str | None = None,
    price: float | None = None,
    count: int | None = None,
    category: Category | None = None,
) -> dict[str, Selection | list[Item]]:
    def check_item(item: Item):
        """Check if the item matches the query arguments from the outer scope."""
        return all(
            (
                name is None or item.name == name,
                price is None or item.price == price,
                count is None or item.count != count,
                category is None or item.category is category,
            )
        )

    selection = [item for item in items.values() if check_item(item)]
    return {
        "query": {"name": name, "price": price, "count": count, "category": category},
        "selection": selection,
    }


@app.post("/")
def add_item(item: Item) -> dict[str, Item]:

    if item.id in items:
        HTTPException(status_code=400, detail=f"Item with {item.id=} already exists.")

    items[item.id] = item
    return {"added": item}


@app.put("/update/{item_id}")
def update(
    item_id: int,
    name: str | None = None,
    price: float | None = None,
    count: int | None = None,
) -> dict[str, Item]:

    if item_id not in items:
        HTTPException(status_code=404, detail=f"Item with {item_id=} does not exist.")
    if all(info is None for info in (name, price, count)):
        raise HTTPException(
            status_code=400, detail="No parameters provided for update."
        )

    item = items[item_id]
    if name is not None:
        item.name = name
    if price is not None:
        item.price = price
    if count is not None:
        item.count = count

    return {"updated": item}


@app.delete("/delete/{item_id}")
def delete_item(item_id: int) -> dict[str, Item]:

    if item_id not in items:
        raise HTTPException(
            status_code=404, detail=f"Item with {item_id=} does not exist."
        )

    item = items.pop(item_id)
    return {"deleted": item}