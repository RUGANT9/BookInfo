from db_models.user import User
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
) -> Optional[User]:
    return (
        db_session.query(User)
        .filter(User.id == id)
        .first()
    )


def get_by_username(
    db_session: Session, *, username: str
) -> Optional[List[User]]:
    return (
        db_session.query(User)
        .filter(User.username == username)
        .all()
    )


def get_by_email(
    db_session: Session, *, mail: str
) -> Optional[List[User]]:
    return (
        db_session.query(User)
        .filter(User.mail_id == mail)
        .all()
    )
