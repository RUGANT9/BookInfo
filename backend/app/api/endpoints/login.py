from models.user import UserCreate
from fastapi import APIRouter
from crud.user import create
from models.user import User as model


router = APIRouter()


@router.get("/")
async def read_items(username: str = None, password: str = None):
    if username == "admin" and password == "adminlogin":
        return "authenticated"
    else:
        return False


@router.post("/")
def sign_up(user: model):
    user_new = UserCreate(**user)
    create()
    return {"msg": "Success"}
