from typing import List
from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI(title="Trading_app")


class Trade(BaseModel):
    id: int
    user_id: int
    currency: str
    size: str
    price: float
    amount: float


users = [
    {'id': 1, 'name': 'John', 'role': 'admin'},
    {'id': 2, 'name': 'San', 'role': 'investor'},
    {'id': 3, 'name': 'Peter', 'role': 'trader'},
]

fake_trades = []


@app.get("/users/{user_id}")
def get_user(user_id: int):
    return [user for user in users if user.get('id') == user_id]


@app.post("/users/{user_id}")
def change_user_name(user_id: int, new_name: str):
    current_user = list(filter(lambda user: user.get("id") == user_id, users))
    if current_user:
        current_user[0]['name'] = new_name
        return {"status": 200, "data": current_user}
    else:
        return {"status": 500}


@app.post("/trades")
def add_post(trades: List[Trade]):
    fake_trades.extend(trades)
    return {"status": 200, "data": fake_trades}


