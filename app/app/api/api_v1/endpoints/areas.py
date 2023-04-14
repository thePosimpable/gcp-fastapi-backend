import math

from typing import List, Any, Optional
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import models, schemas
from app.api import deps
from app.core.config import settings

router = APIRouter()

@router.get("/", response_model = Any)
def get_areas(*, db: Session = Depends(deps.get_db), page: Optional[int] = 1, searchBy: Optional[str] = None, searchByValue: Optional[str] = None, orderBy: Optional[str] = None, orderDir: Optional[str] = None):
	pageSize = settings.PAGINATION_SIZE if page else settings.PAGINATION_MAXSIZE
	offset = (page - 1)*pageSize
	order_by = models.Area.created_at.desc()

	query = db.query(models.Area)

	if searchBy and searchByValue:
		query = query.filter(getattr(models.Area, searchBy).like(f"%{searchByValue}%"))

	if orderBy and orderDir:
		order_by = getattr(models.Area, orderBy).asc() if orderDir == "asc" else getattr(models.Area, orderBy).desc()

	base_areas = query.order_by(order_by).offset(offset).limit(pageSize).all()
	
	querycount = len(base_areas)

	maxpage_divisor = pageSize if page else (1 if querycount == 0 else querycount)

	return {
		"areas": base_areas,
		"querycount": querycount,
		"maxpages": math.ceil(db.query(models.Area).count()/maxpage_divisor)
	}

@router.get("/{areaid}", response_model = schemas.Area)
def get_area(*, db: Session = Depends(deps.get_db), areaid: int):
	base_area = db.query(models.Area).filter(models.Area.areaid == areaid).first()

	if base_area is None:
		raise HTTPException(status_code = 404, detail = "Area not found")

	return base_area

@router.post("/", response_model = schemas.Area)
def add_area(*, db: Session = Depends(deps.get_db), area: schemas.AreaCreate):
	base_area = models.Area(arearepname = area.arearepname, arealocation = area.arealocation, areadaysallowance = area.areadaysallowance)

	db.add(base_area)
	db.commit()
	db.refresh(base_area)
	
	return base_area

@router.delete("/{areaid}", response_model = Any)
def delete_area(*, db: Session = Depends(deps.get_db), areaid: int):
	base_area = db.query(models.Area).filter(models.Area.areaid == areaid).first()

	if not base_area:
		raise HTTPException(status_code = 404, detail = "Area not found")

	db.delete(base_area)
	db.commit()

	return base_area

@router.put("/{areaid}", response_model = Any)
def edit_area(*, db: Session = Depends(deps.get_db), areaid: int, request_area: schemas.Area):
	base_area = db.query(models.Area).filter(models.Area.areaid == areaid).first()
	base_area.arearepname = request_area.arearepname
	base_area.arealocation = request_area.arealocation
	base_area.areadaysallowance = request_area.areadaysallowance
	db.commit()
	db.refresh(base_area)

	return base_area