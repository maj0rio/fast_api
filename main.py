from trading_app.api.models.models import Trade, User
from typing import List

from fastapi import FastAPI

app = FastAPI(title="Trading_app")


fake_trades = [
    {'id': 10, 'user_id': 2, 'currency': 'BTC', 'size': ':)', 'price': 22181.1, 'amount': 3.2},
    {'id': 15, 'user_id': 3, 'currency': 'NEAR', 'size': ':)', 'price': 3.18, 'amount': 301.2},
    {'id': 23, 'user_id': 1, 'currency': 'ETH', 'size': ':)', 'price': 1892.51, 'amount': 14.2},
]


users = [
    {'id': 1, 'name': 'John', 'role': 'admin'},
    {'id': 2, 'name': 'San', 'role': 'investor'},
    {'id': 3, 'name': 'Peter', 'role': 'trader', 'degree': [
        {'id': 1, 'created_at': '2020-01-01T00:00:00', 'type_degree': 'junior'}
    ]},
]


@app.get("/users/{user_id}", response_model=List[User])
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
