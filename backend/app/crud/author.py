from db_models.author import Author
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
) -> Optional[Author]:
    return (
        db_session.query(Author)
        .filter(Author.id == id)
        .first()
    )


def get_author_by_name(
    db_session: Session, *, author_name: str
) -> Optional[List[Author]]:
    return (
        db_session.query(Author)
        .filter(Author.name == author_name)
        .all()
    )


def get_author_by_email(
    db_session: Session, *, mail: str
) -> Optional[List[Author]]:
    return (
        db_session.query(Author)
        .filter(Author.mail_id == mail)
        .all()
    )
