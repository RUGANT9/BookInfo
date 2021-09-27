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
        .filter(Book.id == id)
        .first()
    )


def get_by_book_name(
    db_session: Session, *, name: str
) -> Optional[List[Book]]:
    return (
        db_session.query(Book)
        .filter(Book.name == name)
        .all()
    )


def get_by_author_name(
    db_session: Session, *, name: str
) -> Optional[List[Book]]:
    return (
        db_session.query(Book)
        .filter(Book.author == name)
        .all()
    )


def get_by_publisher_name(
    db_session: Session, *, name: str
) -> Optional[List[Book]]:
    return (
        db_session.query(Book)
        .filter(Book.publisher == name)
        .all()
    )
