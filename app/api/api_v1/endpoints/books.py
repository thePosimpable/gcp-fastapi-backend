from fastapi import APIRouter, Depends, HTTPException, status
from typing import List, Any, Optional
from sqlalchemy.orm import Session

from app import models, schemas
from app.api import deps
from app.core.config import settings
from app.util.shared_funcs import generate_resource_404_message

router = APIRouter()
API_RESOURCE: str = 'book'

@router.get("/", response_model = List[schemas.Book], status_code = status.HTTP_200_OK)
def get_books(*, db: Session = Depends(deps.get_db)):
	query = db.query(models.Book)
	return query.all()

@router.get("/{book_id}", response_model = schemas.Book, status_code = status.HTTP_200_OK)
def get_book(*, db: Session = Depends(deps.get_db), book_id: int):
	resource = db.query(models.Book).filter(models.Book.book_id == book_id).first()

	if resource is None:
		raise HTTPException(
			status_code = status.HTTP_404_NOT_FOUND, 
			detail = generate_resource_404_message(API_RESOURCE)
		)

	return resource

@router.post("/", response_model = schemas.Book, status_code = status.HTTP_201_CREATED)
def add_book(*, db: Session = Depends(deps.get_db), book: schemas.BookCreate):
	new_resource = models.Book(
		title = book.title, 
		rating = book.rating, 
	)

	db.add(new_resource)
	db.commit()
	db.refresh(new_resource)
	
	return new_resource

@router.delete("/{book_id}", response_model = Any, status_code = status.HTTP_200_OK)
def delete_book(*, db: Session = Depends(deps.get_db), book_id: int):
	resource = db.query(models.Book).filter(models.Book.book_id == book_id).first()

	if not resource:
		raise HTTPException(
			status_code = status.HTTP_404_NOT_FOUND, 
			detail = generate_resource_404_message(API_RESOURCE)
		)

	db.delete(resource)
	db.commit()

	return resource

@router.put("/{book_id}", response_model = Any, status_code = status.HTTP_200_OK)
def edit_book(*, db: Session = Depends(deps.get_db), book_id: int, payload_object: schemas.Book):
	resource = db.query(models.Book).filter(models.Book.book_id == book_id).first()

	if not resource:
		raise HTTPException(
			status_code = status.HTTP_404_NOT_FOUND, 
			detail = generate_resource_404_message(API_RESOURCE)
		)

	resource.title = payload_object.title
	resource.rating = payload_object.rating

	db.commit()
	db.refresh(resource)

	return resource