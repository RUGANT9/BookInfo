from pydantic import BaseModel, Field


class UserBase(BaseModel):
    username: str = Field(None, title="username of user", example="John")
    password: str = Field(None, title="password of user", example="Doe")
    mail_id: str = Field(None, title="email of the user", example="John@xyz.com")


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
