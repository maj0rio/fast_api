from fastapi import FastAPI

app = FastAPI(
    title="Trading_app"
)

users = [
    {'id': 1, 'name': 'John', 'role': 'admin'},
    {'id': 2, 'name': 'San', 'role': 'investor'},
    {'id': 3, 'name': 'Peter', 'role': 'trader'},
]


@app.get("/users/{user_id}")
def get_user(user_id: int):
    return [user for user in users if user.get('id') == user_id]


@app.post("/users/{user_id}")
def change_user_name(user_id: int, new_name: str):
    current_user = list(filter(lambda user: user.get("id") == user_id, users))[0]
    current_user['name'] = new_name
    return {"status": 200, "data": current_user}


