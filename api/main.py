from typing import Optional
from models.models import Users, Roles
from fastapi import FastAPI


app = FastAPI(title="Trading_app")


@app.get("/users/{user_id}", response_model=Optional[list[Users]])
def get_user(user_id: int):
    content = [user for user in users if user.get('id') == user_id]
    if content:
        return content
    else:
        return None


@app.post("/users/{user_id}")
def change_user_name(user_id: int, new_name: str):
    current_user = list(filter(lambda user: user.get("id") == user_id, users))
    if current_user:
        current_user[0]['name'] = new_name
        return {'status_code': 200, 'content': current_user}
    else:
        return {'status_code': 400, 'content': None}


# @app.post("/trades")
# def add_post(trades: List[Trade]):
#     fake_trades.extend(trades)
#     return {"status": 200, "data": fake_trades}
