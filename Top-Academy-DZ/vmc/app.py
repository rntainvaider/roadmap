import json
from typing import Any
from uuid import uuid4

import anyio
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, TypeAdapter

USERS_FILE_PATH = "users.json"

app = FastAPI()


class UserIn(BaseModel):
    first_name: str
    last_name: str
    phone_number: str


class User(UserIn):
    id: str


UsersAdapter = TypeAdapter(dict[str, User])


@app.get("/users/")
async def get_users() -> dict[str, User]:
    return UsersAdapter.validate_python(await _load_users_data_from_json())


@app.get("/users/{id_}")
async def get_user(id_: str) -> User:
    users = UsersAdapter.validate_python(await _load_users_data_from_json())
    if id_ not in users:
        raise HTTPException(status_code=404, detail="User not found")
    return users[id_]


@app.post("/users/")
async def create_user(user_in: UserIn) -> User:
    user = User(
        id=str(uuid4()),
        first_name=user_in.first_name,
        last_name=user_in.last_name,
        phone_number=user_in.phone_number,
    )
    await _save_user_to_json(user)
    return user


async def _load_users_data_from_json() -> dict[str, dict[str, Any]]:
    path = anyio.Path(USERS_FILE_PATH)
    if not await path.exists() or (await path.stat()).st_size == 0:
        return {}

    async with await path.open() as file:
        data = await file.read()

    return json.loads(data)


async def _save_user_to_json(user: User) -> None:
    data = await _load_users_data_from_json()
    data[user.id] = user.model_dump()
    async with await anyio.Path(USERS_FILE_PATH).open("w") as file:
        _ = await file.write(json.dumps(data, indent=4))
