from fastapi import APIRouter, Depends, HTTPException
from typing import List, Any, Optional
from sqlalchemy.orm import Session

# from app import models, schemas
# from app.api import deps
from app.core.config import settings

router = APIRouter()

@router.get("/", response_model = Any)
# def get_testbase(*, db: Session = Depends(deps.get_db), page: Optional[int] = 1, searchBy: Optional[str] = None, searchByValue: Optional[str] = None, orderBy: Optional[str] = None, orderDir: Optional[str] = None):
def get_testbase():
	return {"message": "test world base"}