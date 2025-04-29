from pydantic import BaseModel, Field
from typing import List, Optional
from enum import IntEnum, Enum
from fastapi import FastAPI, HTTPException
import pandas as pd
from datetime import datetime

# uvicorn neural_api:api --reload
# fastapi dev fast_api_data.py --port 9999
# http://127.0.0.1:8000/docs         for docs and UI

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
oil = oil_clean.head()



# Schema
class OilPrice(BaseModel):
    price_id: int
    date: datetime
    price: float
    euro_price: float

# For PUT endpoint
class OilPriceUpdate(OilPrice):
    date: Optional[datetime] = Field(None, min_length=3, max_length=512, description='Date')
    price: Optional[float] = Field(None, min_length=3, max_length=512, description='Price')
    euro_price: Optional[float] = Field(None, min_length=3, max_length=512, description='Euro Price')

# fill in list comprehension
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

# get all prices up until n index, or all of them
@app.get('/prices', response_model=List[OilPrice])
def get_prices(n: int = None):
    if n:
        return all_prices[:n]
    else:
        return all_prices
    

# get price by id
@app.get('/prices/{price_id}', response_model=OilPrice)
def get_price_id(price_id: int):
    for price in all_prices:
        if price.price_id == price_id:
            return price
    raise HTTPException(status_code=404, detail='Price not found')


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