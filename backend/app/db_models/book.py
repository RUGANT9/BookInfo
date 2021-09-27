from sqlalchemy import Column, Integer, String, Table
from sqlalchemy.ext.declarative import declarative_base
from db.base_class import Base

class Book(Base):
    __tablename__ = "book"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    author = Column(String)
    publisher = Column(String)

    class Config:
        orm_mode = True