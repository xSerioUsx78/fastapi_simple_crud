from fastapi import Depends, FastAPI, HTTPException, status
from sqlalchemy.orm import Session
from db import crud, models, schemas
from db.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI(debug=True)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def root():
    return {'Info': "Basic CRUD API app"}


@app.get("/posts/", response_model=schemas.PostList)
def get_posts(offset: int = 0, limit: int = 20, db: Session = Depends(get_db)):
    db_posts = crud.get_posts(db, offset, limit)
    data = {
        'results': db_posts,
        'count': db.query(models.Post).count()
    }
    return data


@app.post('/posts/create/', status_code=status.HTTP_201_CREATED, response_model=schemas.PostCreate)
def create_post(post: schemas.PostCreate, db: Session = Depends(get_db)):
    db_post = crud.create_post(db, post)
    return db_post


@app.get('/posts/{id}/', response_model=schemas.Post)
def get_post(id: int, db: Session = Depends(get_db)):
    db_post = crud.get_post(db, id)
    if db_post is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND,
                            detail="The post not find.")
    return db_post
