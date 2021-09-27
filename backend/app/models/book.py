from typing import Optional
from pydantic import BaseModel, Field


class BookBase(BaseModel):
    name: Optional[str] = Field(None, title="Name of the book", example="Kane and Abel")
    author: Optional[str] = Field(None, title="Author of the book", example="Jeffrey Archer")
    publisher: Optional[str] = Field(None, title="Publisher of the book", example="Penguin")


class BookUpdate(BookBase):
    pass


class BookinDB(BookBase):
    id: int


class BookCreate(BookBase):
    pass


class Book(BookBase):
    pass
