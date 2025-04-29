import pandas as pd
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from datetime import date



app = FastAPI()


# Load CSV into a DataFrame
try:
    df = pd.read_csv('transactions.csv', header=0, delimiter=',')
except Exception as error:
    print('Error loading csv', error)
    df = pd.DataFrame()

# Check the first few rows to confirm how the columns look
print(df.head())


# # Convert DataFrame to list of dicts (like JSON records)
# transactions = df.to_dict(orient='records')

transactions = []
for _, row in df.iterrows():
    transaction = {
        "date": row['date'],        # Column 0 (index 0) is date
        "store_number": int(row['store_nbr']), # Column 1 (index 1) is store number
        "transactions": int(row['transactions'])        # Column 2 (index 2) is value
    }
    transactions.append(transaction)


@app.get('/')
def index():
    return {"transactions": transactions}


@app.get('/transactions/by_date')
def get_transactions_by_date(date: str):
    store_date = [tx for tx in transactions if tx['date'] == date]

    if store_date:
        return {'transaction': store_date}
    raise HTTPException(status_code=404, detail='Date not found')


@app.get('/transactions/search')
def get_transactions_by_store_and_by_date(date: str, store_number: int):
    result = [tx for tx in transactions if tx['date'] == date and tx['store_number'] == store_number]
    if result:
        return {'transactions': result}
    raise HTTPException(status_code=404, detail='Transaction not found')


@app.get('/transactions/{store_number}')
def get_transactions_by_store(store_number: int):
    # Find all transactions for the given store_number
    store_transactions = [tx for tx in transactions if tx['store_number'] == store_number]

    # If transactions are found for that store_number, return them
    if store_transactions:
        return {"transactions": store_transactions}
    
    # If no transactions are found for the store_number, raise an HTTP 404 error
    raise HTTPException(status_code=404, detail='Transaction not found')









# print(df)
# print(df.dtypes)    # test that there are no lists in the data

# uvicorn main:app -- reload        TO RUN !
