import pandas as pd
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from enum import Enum
from typing import List

# --- Load Data ---
try:
    df = pd.read_csv("transactions.csv")
except Exception as e:
    print("Error loading CSV:", e)
    df = pd.DataFrame(columns=["date", "store_nbr", "transactions"])


# --- Enum for Store Numbers (example with selected stores only) ---
class StoreNumberEnum(int, Enum):
    store_1 = 1
    store_2 = 2
    store_3 = 3


# --- Pydantic Model ---
class Transaction(BaseModel):
    date: str
    store_number: int
    transactions: int


# --- FastAPI App ---
app = FastAPI()


# Convert DataFrame into list of dicts
def get_transactions_data() -> List[Transaction]:
    return [
        Transaction(
            date=row["date"],
            store_number=int(row["store_nbr"]),
            transactions=int(row["transactions"])
        )
        for _, row in df.iterrows()
    ]


@app.get("/", response_model=List[Transaction])
def get_all_transactions():
    return get_transactions_data()


@app.get("/store/{store_number}", response_model=List[Transaction])
def get_transactions_by_store(store_number: StoreNumberEnum):
    data = get_transactions_data()
    results = [tx for tx in data if tx.store_number == store_number.value]

    if not results:
        raise HTTPException(status_code=404, detail="No transactions found for this store.")
    return results
