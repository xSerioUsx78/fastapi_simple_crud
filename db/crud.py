from typing import List, Union
from sqlalchemy import desc
from sqlalchemy.orm import Session
from . import models, schemas


def get_post(db: Session, id: int) -> Union[schemas.Post, None]:
    query = db.query(models.Post).filter(models.Post.id == id).first()
    return query


def get_posts(db: Session, offset: int = 0, limit: int = 100) -> List[schemas.Post]:
    query = db.query(models.Post).order_by(desc(models.Post.timestamp)).offset(offset).limit(
        limit).all()
    return query


def create_post(db: Session, post: schemas.PostCreate) -> schemas.Post:
    db_post = models.Post(**post.dict())
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post
