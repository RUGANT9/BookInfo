from typing import Optional
from pydantic import BaseModel, Field


class UserBase(BaseModel):
    username: str = Field(None, title="", example="")
    password: str = Field(None, title="", example="")
    mail_id: str = Field(None, title="", example="")


class UserUpdate(UserBase):
    pass


class UserinDB(UserBase):
    id: int


class UserCreate(UserBase):
    pass


class User(UserBase):
    pass


class UserLogin(BaseModel):
    username: str
    password: str
