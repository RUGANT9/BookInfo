from sqlalchemy import Column, String
from sqlalchemy.sql.sqltypes import Integer
from db.base_class import Base


class Author(Base):
    __tablename__ = "author"
    id = Column(Integer)
    name = Column(String)
    mail_id = Column(String)

    class Config:
        orm_mode = True