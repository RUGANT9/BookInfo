from fastapi import Depends, APIRouter
from fastapi.security import OAuth2PasswordBearer

from models.user import User as model


router = APIRouter()


@router.get("/login")
async def read_items(username: str, password: str):
    if username == "admin" and password == "adminlogin":
        return "authenticated"
    else:
        return False


@router.post("/register")
def sign_up(user: model):
    return {"msg":"Success"}
