from typing import List, Union
from sqlalchemy import desc
from sqlalchemy.orm import Session
from . import models, schemas


def get_post(db: Session, id: int) -> Union[schemas.Post, None]:
    objects = db.query(models.Post).filter(models.Post.id == id).first()
    return objects


def get_posts(db: Session, offset: int = 0, limit: int = 100) -> List[schemas.Post]:
    objects = db.query(models.Post).order_by(desc(models.Post.timestamp)).offset(offset).limit(
        limit).all()
    return objects


def create_post(db: Session, post: schemas.PostCreate) -> schemas.Post:
    post = models.Post(**post.dict())
    db.add(post)
    db.commit()
    db.refresh(post)
    return post


def update_post(db: Session, id: int, post: schemas.PostUpdate) -> None:
    post = db.query(models.Post).filter(
        models.Post.id == id
    ).update(post.dict())
    db.commit()