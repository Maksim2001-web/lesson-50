from fastapi import FastAPI, HTTPException, Path
from pydantic import BaseModel
from typing import Dict, Annotated

app = FastAPI()

# Словарь для хранения пользователей
users: Dict[str, str] = {'1': 'Имя: Example, возраст: 18'}

class User(BaseModel):
    username: str
    age: int

@app.get('/users')
async def get_users():
    return users

@app.post('/user/{username}/{age}')
async def create_user(
    username: str,
    age: Annotated[int, Path(..., ge=0)]  # Возраст должен быть больше или равен 0
):
    # Находим максимальный ключ и добавляем нового пользователя
    new_id = str(max(map(int, users.keys()), default=0) + 1)
    users[new_id] = f"Имя: {username}, возраст: {age}"
    return f"User {new_id} is registered"

@app.put('/user/{user_id}/{username}/{age}')
async def update_user(
    user_id: Annotated[str, Path(...)],
    username: str,
    age: Annotated[int, Path(..., ge=0)]  # Возраст должен быть больше или равен 0
):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="Пользователь не найден")

    users[user_id] = f"Имя: {username}, возраст: {age}"
    return f"User {user_id} has been updated"

@app.delete('/user/{user_id}')
async def delete_user(
    user_id: Annotated[str, Path(...)]  # user_id без дополнительных ограничений
):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="Пользователь не найден")

    del users[user_id]
    return f"User {user_id} has been deleted"

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='127.0.0.1', port=8000)

# Запуск приложения
# uvicorn module_16_3:app --reload
