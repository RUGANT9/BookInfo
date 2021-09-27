from db_models.book import Book
from models.book import BookUpdate, BookCreate
from typing import Optional, List
from sqlalchemy.orm import Session


def create(
    db_session: Session, *,
    book_in: BookCreate
) -> Book:
    book = Book(**book_in.dict(exclude_unset=True, exclude={'password'}))
    db_session.add(book)
    try:
        db_session.commit()
    except Exception as e:
        db_session.rollback()
        raise e
    db_session.refresh(book)
    return book


def update(
    db_session: Session, *,
    book_in: BookUpdate, book: Book
) -> Book:
    if book is None:
        return None
    book_data = jsonable_encoder(book)
    update_data = book_in.dict(exclude_unset=True)
    for field in update_data:
        if field in book_data:
            setattr(book, field, update_data[field])

    db_session.add(book)
    try:
        db_session.commit()
    except Exception as e:
        raise e
    db_session.refresh(book)
    return book


def delete(
    db_session: Session, *, id: int
) -> Book:
    book = db_session.query(Book).filter(Book.id == id).first()
    db_session.delete(book)
    db_session.commit()
    return book


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
