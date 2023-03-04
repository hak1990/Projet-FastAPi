#System imports

#Libs imports
from fastapi import APIRouter, status, Response

#Local imports
from internal.models import User

router = APIRouter()

# bellow is a first way to instantiate a list of data. Here we instantiate them as dicts
users = [
    {"id": 1, "name": "test1", "password_hash": "b7e507f7b30caff568e11c613de215eba2f861b8545ef8c30298fdf9ddcd97e8", "password": "bambi"},
    {"id": 2, "name": "test2", "password_hash": "467baa6c1a9337043bbf7837b4ab15022f8d5002c10947a844112ae988a5e910", "password": "johnDoe"},
    {"id": 4, "name": "test4", "password_hash": "57d96f829f4d296f5553126cf31a6939c36ba45fc397fd80274d67239c5322a9", "password": "Casper"},
    {"id": 3, "name": "test3", "password_hash": "742f552b7848035dc31cc11cda62d5eada07fc53ba17b9a18097a83bed055847", "password": "Beverlyhills"}
]




@router.get("/users")
async def get_all_users() -> list[User]:
    return users


@router.get("/users/search")
async def search_users(name: str):
    return list(filter(lambda x: x["name"] == name, users))

@router.get("/users/{user_id}")
async def get_user_by_id(user_id: int, name: str | None = None):
    filtred_list = list(filter(lambda x: x["id"] == user_id, users))
    if name is not None:
        filtred_list = list(filter(lambda x: x["name"] == name, users))
    return filtred_list

@router.post("/users", status_code=status.HTTP_201_CREATED)
async def create_user(user: User) -> User:
    users.append(user)
    return user

@router.delete("/users/{user_id}")
async def delete_user(user_id: int) -> User:
    deleted_user = list(filter(lambda x: x["id"] == user_id, users))
    users.remove(deleted_user[0])
    return deleted_user[0]


@router.put("/users/{user_id}")
async def put_user(user_id: int, user: User) -> User:
    for i in range(0, len(users)):
        if users[i]["id"] == user_id:
            users[i] = user.__dict__ # The .__dict__ is needed because we decided to init our list as dicts
    return Response(status_code = status.HTTP_200_OK)
    # no need to return anything in a PUT, a 200 will be returned by default