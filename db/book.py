from sqlalchemy import Column, Integer, String, Table
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

book = Table(
    "book",
    Base.metadata,
)


class Book(Base):
    __tablename__ = "book"
    book_id = Column(Integer, primary_key=True)
    book_name = Column(String)
