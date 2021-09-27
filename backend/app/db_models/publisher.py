from sqlalchemy import Column, String
from db.base_class import Base


class Publisher(Base):
    __tablename__ = "publisher"
    name = Column(String)
    mail_id = Column(String)

    class Config:
        orm_mode = True