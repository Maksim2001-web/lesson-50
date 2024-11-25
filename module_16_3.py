from fastapi import FastAPI
from typing import Dict

app = FastAPI()

# Словарь для имитации базы данных
users: Dict[str, str] = {'1': 'Имя: Example, возраст: 18'}

# GET запрос по маршруту '/users'
@app.get("/users")
async def get_users():
    """Возвращает словарь users."""
    return users

# POST запрос по маршруту '/user/{username}/{age}'
@app.post("/user/{username}/{age}")
async def create_user(username: str, age: int):
    """Добавляет в словарь users по максимальному по значению ключом значение строки"""
    max_id = max(int(key) for key in users.keys())
    user_id = max_id + 1
    users[str(user_id)] = f"Имя: {username}, возраст: {age}"
    return f"User {user_id} is registered"

# PUT запрос по маршруту '/user/{user_id}/{username}/{age}'
@app.put("/user/{user_id}/{username}/{age}")
async def update_user(user_id: str, username: str, age: int):
    """Обновляет значение из словаря users под ключом user_id."""
    if user_id in users:
        users[user_id] = f"Имя: {username}, возраст: {age}"
        return f"User {user_id} has been updated"
    else:
        return "User not found"

# DELETE запрос по маршруту '/user/{user_id}'
@app.delete("/user/{user_id}")
async def delete_user(user_id: str):
    """Удаляет из словаря users по ключу user_id."""
    if user_id in users:
        del users[user_id]
        return f"User {user_id} has been deleted"
    else:
        return "User not found"

