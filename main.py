from fastapi import Depends, FastAPI, HTTPException, status
from sqlalchemy.orm import Session
from db import crud, models, schemas
from db.database import SessionLocal, engine
from utils import shortcuts

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
    objects = crud.get_posts(db, offset, limit)
    data = {
        'results': objects,
        'count': db.query(models.Post).count()
    }
    return data


@app.post('/posts/create/', status_code=status.HTTP_201_CREATED, response_model=schemas.Post)
def create_post(post: schemas.PostCreate, db: Session = Depends(get_db)):
    obj = crud.create_post(db, post)
    return obj


@app.put('/posts/{id}/')
def update_post(id: int, post: schemas.PostUpdate, db: Session = Depends(get_db)):
    crud.update_post(db, id, post)
    return None


@app.get('/posts/{id}/', response_model=schemas.Post)
def get_post(id: int, db: Session = Depends(get_db)):
    obj = crud.get_post(db, id)
    shortcuts.get_object_or_404(obj)
    return obj