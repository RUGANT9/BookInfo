from db_models.book import Book
from typing import Optional, List
from sqlalchemy.orm import Session


def create():
    pass


def update():
    pass


def delete():
    pass


def get_by_id(
    db_session: Session, *, id: int
) -> Optional[Book]:
    return (
        db_session.query(Book)
        .filter(Book.book_id == id)
        .first()
    )


def get_by_book_name(
    db_session: Session, *, name: str
) -> Optional[List[Book]]:
    return (
        db_session.query(Book)
        .filter(Book.book_name == name)
        .all()
    )


def get_by_author_name(
    db_session: Session, *, name: str
) -> Optional[List[Book]]:
    return (
        db_session.query(Book)
        .filter(Book.book_author == name)
        .all()
    )


def get_by_publisher_name(
    db_session: Session, *, name: str
) -> Optional[List[Book]]:
    return (
        db_session.query(Book)
        .filter(Book.book_publisher == name)
        .all()
    )
