from pydantic import BaseModel, Field
from typing import List, Optional
from fastapi import FastAPI, HTTPException
import pandas as pd
from datetime import date, datetime

# HOW TO RUN

# fastapi dev main.py
# OR
# uvicorn main:app --reload

# for UI and docs
# http://127.0.0.1:8000/docs
         


app = FastAPI()

# import oil prices data
oil = pd.read_csv('oil.csv')

# rename columns
oil.columns = ['date', 'price']

# add an euro price column
oil['euro price'] = oil['price'] * 1.1

# fill NaN values with 0
oil_clean = oil.fillna(0)

# will take first 5 entries for example
oil = oil_clean.head(5)


# Schema
class OilPrice(BaseModel):
    price_id: int
    date: date
    price: float
    euro_price: float

# For PUT endpoint
class OilPriceUpdate(OilPrice):
    price_id: Optional[int]
    date: Optional[date] 
    price: Optional[float] 
    euro_price: Optional[float] 

# transfer to working format
all_prices = [
    OilPrice(
        price_id = index + 1,
        date = row['date'], 
        price = row['price'], 
        euro_price = row['euro price']
    )
    for index, row in oil.iterrows()
]


# ENDPOINTS

# get all records | up until n index | search by parameter
@app.get('/prices', response_model=List[OilPrice])
def query_item_by_price(
    n: int | None = None,
    price_id: int | None = None,
    date: date | None = None,
    price: float | None = None,
    euro_price: float | None = None):
    # for outer scope
    def check_price(oil_price: OilPrice):
        return all(
            (
                price_id is None or oil_price.price_id == price_id, 
                date is None or oil_price.date == date, 
                price is None or oil_price.price == price, 
                euro_price is None or oil_price.euro_price == euro_price 

            )
        )
    result = [oil_price for oil_price in all_prices if check_price(oil_price)]
    return result[:n] if n is not None else result
    

# get record by id
@app.get('/prices/{price_id}', response_model=OilPrice)
def get_price_id(price_id: int):
    for price in all_prices:
        if price.price_id == price_id:
            return price
    raise HTTPException(status_code=404, detail='Price not found')


# add a new record
@app.post('/prices', response_model=OilPrice)
def create_price(price: OilPrice):
    new_price_id = max(price.price_id for price in all_prices) + 1

    new_price = OilPrice(
        price_id = new_price_id,
        date = price.date,
        price = price.price,
        euro_price = price.euro_price,
    )
    all_prices.append(new_price)
    return new_price


# update a record
@app.put('/prices/{price_id}', response_model=OilPriceUpdate)
def update_price(price_id: int, updated_price: OilPriceUpdate):
    for price in all_prices:
        if price.price_id == price_id:
            if updated_price.date is not None:
                price.date = updated_price.date
            if updated_price.price is not None:
                price.price = updated_price.price
            if updated_price.euro_price is not None:
                price.euro_price = updated_price.euro_price
            return price
        
    raise HTTPException(status_code=404, detail='Record not found') 


# delete a record
@app.delete('/prices/{price_id}', response_model=OilPrice)
def detete_price(price_id: int):
    for index, price in enumerate(all_prices):
        if price.price_id == price_id:
            deleted_price = all_prices.pop(index)
            return deleted_price
        
    raise HTTPException(status_code=404, detail='Record not found')




