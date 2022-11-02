from typing import Optional, List
from datetime import datetime
from pydantic import BaseModel


class PostBase(BaseModel):
    title: str
    description: Optional[str] = None


class PostCreate(PostBase):
    pass

class PostUpdate(PostBase):
    pass

class Post(PostBase):
    id: int
    timestamp: datetime

    class Config:
        orm_mode = True

class PostListResults(PostBase):
    id: int
    timestamp: datetime

    class Config:
        orm_mode = True

class PostList(BaseModel):
    results: List[PostListResults]
    count: int