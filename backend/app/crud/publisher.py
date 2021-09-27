from db_models.publisher import Publisher
from typing import Optional, List
from sqlalchemy.orm import Session


def create():
    pass


def update():
    pass


def delete():
    pass


def get_publisher_by_id(
    db_session: Session, *, id: int
) -> Optional[Publisher]:
    return (
        db_session.query(Publisher)
        .filter(Publisher.id == id)
        .first()
    )


def get_publisher_by_name(
    db_session: Session, *, name: str
) -> Optional[List[Publisher]]:
    return (
        db_session.query(Publisher)
        .filter(Publisher.name == name)
        .all()
    )


def get_publisher_by_email(
    db_session: Session, *, mail: str
) -> Optional[List[Publisher]]:
    return (
        db_session.query(Publisher)
        .filter(Publisher.mail_id == mail)
        .all()
    )
