from models.user import UserCreate, UserUpdate
from db_models.user import User
from typing import Optional, List
from sqlalchemy.orm import Session
from db_models.user import User


def create(
    db_session: Session, *,
    user_in: UserCreate
) -> User:
    user = User(**user_in.dict(exclude_unset=True, exclude={'password'}))
    db_session.add(user)
    try:
        db_session.commit()
    except Exception as e:
        db_session.rollback()
    db_session.refresh(user)
    return user


def update(
    db_session: Session, *,
    user_in: UserUpdate, user: User
) -> User:
    if user is None:
        return None
    user_data  = jsonable_encoder(user)
    update_data = user_in.dict(exclude_unset=True)
    for field in update_data:
        if field in user_data:
            setattr(user, field, update_data[field])



def delete():
    pass


def ge_user_by_id(
    db_session: Session, *, id: int
) -> Optional[User]:
    return (
        db_session.query(User)
        .filter(User.id == id)
        .first()
    )


def get_user_by_username(
    db_session: Session, *, username: str
) -> Optional[List[User]]:
    return (
        db_session.query(User)
        .filter(User.username == username)
        .all()
    )


def get_user_by_email(
    db_session: Session, *, mail: str
) -> Optional[List[User]]:
    return (
        db_session.query(User)
        .filter(User.mail_id == mail)
        .all()
    )
