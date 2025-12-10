from fastapi import FastAPI, Depends, HTTPException 
from sqlalchemy.orm import Session
from sqlalchemy import select, and_
from typing import Annotated, Optional, List 

from database import SessionLocal, BooksModel, Base, engine 
from schemas import BookBase, Book
Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

SessionDep = Annotated[Session, Depends(get_db)]

app = FastAPI()


@app.get(
    "/books",
    tags=["Books"],
    summary="Get all books",
    response_model=List[Book]
)
def get_books(session: SessionDep): 
    statement = select(BooksModel)
    books = session.scalars(statement).all() 
    return books


@app.post(
    "/books",
    tags=["Books"],
    description="Add a new book",
    response_model=Book 
)
def add_book(book: BookBase, session: SessionDep):
    db_book = BooksModel(**book.model_dump()) 
    session.add(db_book)
    session.commit()
    session.refresh(db_book)
    return db_book


@app.delete("/books/{book_id}")
def delete_book(book_id: int, session: SessionDep):
    db_book = session.get(BooksModel, book_id)
    if db_book is None:
        raise HTTPException(status_code=404, detail=f"Книга с ID {book_id} не найдена.")
    session.delete(db_book)
    session.commit()
    return {"message": f"Книга с ID {book_id} успешно удалена."}


@app.put(
    "/books/{book_id}",
    tags=["Books"],
    summary="Update book details",
    response_model=Book
)
def update_book(book_id: int, new_data: BookBase, session: SessionDep):
    db_book = session.get(BooksModel, book_id)
    
    if db_book is None:
        raise HTTPException(status_code=404, detail=f"Книга с ID {book_id} не найдена.")

    update_data = new_data.model_dump(exclude_unset=True) 
    for key, value in update_data.items():
        setattr(db_book, key, value) 

    
    session.commit()
    session.refresh(db_book)
    return db_book


@app.get(
    "/books/search",
    tags=["Books"],
    summary="Search books by title, author, or year",
    response_model=List[Book]
)
def search_books(
    title: Optional[str] = None, 
    author: Optional[str] = None, 
    year: Optional[int] = None, 
    session: SessionDep = None 
):
    statement = select(BooksModel)
    conditions = []
    
    if title is not None:
        conditions.append(BooksModel.title.ilike(f'%{title}%')) 

    if author is not None:
        conditions.append(BooksModel.author.ilike(f'%{author}%')) 

    if year is not None:
        conditions.append(BooksModel.year == year) 
    

    if conditions:
        statement = statement.where(and_(*conditions)) 
        
    books = session.scalars(statement).all()
    return books