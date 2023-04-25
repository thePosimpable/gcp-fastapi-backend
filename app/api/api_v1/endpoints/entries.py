from fastapi import APIRouter, Depends, HTTPException, status
from typing import List, Any, Optional
from sqlalchemy.orm import Session

from app import models, schemas
from app.api import deps
from app.core.config import settings
from app.util.shared_funcs import generate_resource_404_message

router = APIRouter()
API_RESOURCE: str = 'entry'

@router.get("/", response_model = List[schemas.Entry], status_code = status.HTTP_200_OK)
def get_entries(*, db: Session = Depends(deps.get_db)):
	query = db.query(models.Entry)
	return query.all()

@router.get("/{entry_id}", response_model = schemas.Entry, status_code = status.HTTP_200_OK)
def get_entry(*, db: Session = Depends(deps.get_db), entry_id: int):
	resource = db.query(models.Entry).filter(models.Entry.entry_id == entry_id).first()

	if resource is None:
		raise HTTPException(
			status_code = status.HTTP_404_NOT_FOUND, 
			detail = generate_resource_404_message(API_RESOURCE)
		)

	return resource

@router.post("/", response_model = schemas.Entry, status_code = status.HTTP_201_CREATED)
def add_book(*, db: Session = Depends(deps.get_db), entry: schemas.EntryCreate):
	new_resource = models.Entry(
		title = entry.title, 
		description = entry.description,
		start_date = entry.start_date,
		end_date = entry.end_date,
		color = entry.color,
		icon = entry.icon,
	)

	db.add(new_resource)
	db.commit()
	db.refresh(new_resource)
	
	return new_resource

@router.delete("/{entry_id}", response_model = Any, status_code = status.HTTP_200_OK)
def delete_book(*, db: Session = Depends(deps.get_db), entry_id: int):
	resource = db.query(models.Entry).filter(models.Entry.entry_id == entry_id).first()

	if not resource:
		raise HTTPException(
			status_code = status.HTTP_404_NOT_FOUND, 
			detail = generate_resource_404_message(API_RESOURCE)
		)

	db.delete(resource)
	db.commit()

	return resource

@router.put("/{entry_id}", response_model = Any, status_code = status.HTTP_200_OK)
def edit_book(*, db: Session = Depends(deps.get_db), entry_id: int, payload_object: schemas.Entry):
	resource = db.query(models.Entry).filter(models.Entry.entry_id == entry_id).first()

	if not resource:
		raise HTTPException(
			status_code = status.HTTP_404_NOT_FOUND, 
			detail = generate_resource_404_message(API_RESOURCE)
		)

	resource.title = payload_object.title
	resource.description = payload_object.description
	resource.start_date = payload_object.start_date
	resource.end_date = payload_object.end_date
	resource.color = payload_object.color
	resource.icon = payload_object.icon

	db.commit()
	db.refresh(resource)

	return resource