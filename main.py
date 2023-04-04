from fastapi import FastAPI,Depends
from numpy import append
import schemas,models
from database import SessionLocal,engine
from sqlalchemy.orm import Session
from database import engine
from typing import List
import requests
from fastapi import status,HTTPException
from hashing import Hash
from fastapi.security import OAuth2PasswordRequestForm
import Token,oauth2
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

models.Base.metadata.create_all(engine)

app=FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()
@app.post('/books',response_model=schemas.ShowBook,tags = ['book'])
def create_book(request:schemas.Book,db:Session=Depends(get_db)):
    new_book=models.Book(Accessnumber=request.Accessnumber,Title=request.Title,Author=request.Author,Subject=request.Subject,KeyWord=request.KeyWord,bookcategory=request.bookcategory)
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    db.close()
    return new_book



@app.get('/get/book/{Accessnumber}',response_model=schemas.ShowBook,tags=['book'])
def get_book(Accessnumber,db:Session=Depends(get_db)):
    book=db.query(models.Book).filter(models.Book.Accessnumber).first()
    return book

@app.get('/get/book/{Title}',response_model=schemas.ShowBook,tags=['book'])
def get_book(Title,db:Session=Depends(get_db)):
    book=db.query(models.Book).filter(models.Book.Title).first()
    return book

@app.get('/get/book/{Author}',response_model=schemas.ShowBook,tags=['book'])
def get_book(Author,db:Session=Depends(get_db)):
    book=db.query(models.Book).filter(models.Book.Author).first()
    return book

@app.get('/get/book/{Subject}',response_model=schemas.ShowBook,tags=['book'])
def get_book(Subject,db:Session=Depends(get_db)):
    book=db.query(models.Book).filter(models.Book.Subject).first()
    return book

@app.get('/get/book/{Key_word}',response_model=schemas.ShowBook,tags=['book'])
def get_book(KeyWord,db:Session=Depends(get_db)):
    book=db.query(models.Book).filter(models.Book.KeyWord).first()
    return book


@app.get('/book/',response_model=List[schemas.ShowBook],tags=['book'])
def get_book(db:Session=Depends(get_db)):
    book=db.query(models.Book).all()
    return book 


@app.get('/bookcategory/{name}',response_model=List[schemas.ShowBook],tags=['book'])
def get_book(name,db:Session=Depends(get_db)):
    book=db.query(models.Book).filter(models.Book.bookcategory==name).all()
    return book



@app.delete('/book/{Accessnumber}',status_code=status.HTTP_404_NOT_FOUND,tags = ['book'])
def create_book(Accessnumber,db:Session=Depends(get_db)):
    db.query(models.Book).filter(models.Book.Accessnumber==Accessnumber).delete(synchronize_session=False)
    db.commit()
    return 'DONE'


@app.post('/category',response_model=schemas.Category,tags = ['category'])
def create_category(request:schemas.ShowCategory,db:Session=Depends(get_db)):
    new_category=models.Category(id=request.id,bookcategory=request.bookcategory)
    db.add(new_category)
    db.commit()
    db.refresh(new_category)
    db.close()
    return new_category

@app.get('/get/category/{id}',response_model=schemas.ShowBook,tags=['category'])
def get_category(id,db:Session=Depends(get_db)):
    category=db.query(models.Category).filter(models.Category.id).first()
    return category


@app.get('/category/',response_model=List[schemas.Category],tags=['category'])
def get_category(db:Session=Depends(get_db)):
    category=db.query(models.Book).all()
    return category



if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8002, reload=True)