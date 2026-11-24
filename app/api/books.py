from fastapi import APIRouter, Depends, HTTPException, Response
from sqlalchemy.orm import Session

from app.db.db import get_db
from app.db import crud
from app.schemas import BookCreate, BookUpdate, BookResponse

router = APIRouter(prefix="/books", tags=["Books"])


@router.get("/", response_model=list[BookResponse])
def get_books(
    category_id: int | None = None,
    db: Session = Depends(get_db)
):
    return crud.get_books(db, category_id)


@router.get("/{book_id}", response_model=BookResponse)
def get_book(book_id: int, db: Session = Depends(get_db)):
    book = crud.get_book(db, book_id)

    if book is None:
        raise HTTPException(404, "Book not found")

    return book


@router.post("/", response_model=BookResponse, status_code=201)
def create_book(data: BookCreate, db: Session = Depends(get_db)):
    if crud.get_category(db, data.category_id) is None:
        raise HTTPException(404, "Category not found")

    return crud.create_book(db, **data.model_dump())


@router.put("/{book_id}", response_model=BookResponse)
def update_book(
    book_id: int,
    data: BookUpdate,
    db: Session = Depends(get_db)
):
    if crud.get_book(db, book_id) is None:
        raise HTTPException(404, "Book not found")

    if crud.get_category(db, data.category_id) is None:
        raise HTTPException(404, "Category not found")

    return crud.update_book(db, book_id, **data.model_dump())


@router.delete("/{book_id}", status_code=204)
def delete_book(book_id: int, db: Session = Depends(get_db)):
    if not crud.delete_book(db, book_id):
        raise HTTPException(404, "Book not found")

    return Response(status_code=204)