from db_models.author import Author
from typing import Optional, List
from models.author import AuthorCreate, AuthorUpdate
from sqlalchemy.orm import Session


def create(
    db_session: Session, *,
    author_in: AuthorCreate
) -> Author:
    author = Author(**author_in.dict(exclude_unset=True))
    db_session.add(author)
    try:
        db_session.commit()
    except Exception as e:
        db_session.rollback()
        raise e
    db_session.refresh(author)
    return author


def update(
    db_session: Session, *,
    author_in: AuthorUpdate, author: Author
) -> Author:
    if author is None:
        return None
    author_data = jsonable_encoder(author)
    update_data = author_in.dict(exclude_unset=True)
    for field in update_data:
        if field in author_data:
            setattr(author, field, update_data[field])

    db_session.add(author)
    try:
        db_session.commit()
    except Exception as e:
        raise e
    db_session.refresh(author)
    return author


def delete(
    db_session: Session, *, id: int
) -> Author:
    author = db_session.query(Author).filter(Author.id==id).first()
    db_session.delete(author)
    db_session.commit()
    return author


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
