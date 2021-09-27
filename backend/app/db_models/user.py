from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import Integer, String
from db.base_class import Base


class User(Base):
    __tablename__ = "user"
    id = Column(Integer)
    username = Column(String)
    password = Column(String)
    mail_id = Column(String)

    class Config:
        orm_mode = True
