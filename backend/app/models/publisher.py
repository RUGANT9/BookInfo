from typing import Optional
from pydantic import BaseModel, Field


class PublisherBase(BaseModel):
    name: str = Field(None, title="", example="")
    mail_id: str = Field(None, title="", example="")


class PublisherUpdate(PublisherBase):
    pass


class PublisherinDB(PublisherBase):
    id: int


class PublisherCreate(PublisherBase):
    pass


class Publisher(PublisherBase):
    pass

