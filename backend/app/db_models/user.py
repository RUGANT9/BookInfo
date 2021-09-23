from sqlalchemy import Column, String
from db.base_class import Base


class User(Base):
    __tablename__ = "user"
    username = Column(String)
    password = Column(String)
    mail_id = Column(String)

    class Config:
        orm_mode = True
