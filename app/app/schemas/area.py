import datetime
from typing import List, Optional
from pydantic import BaseModel

class AreaBase(BaseModel):
	arearepname: str
	arealocation: str
	areadaysallowance: int
	created_at: Optional[datetime.datetime] = None
	updated_at: Optional[datetime.datetime] = None

class AreaCreate(AreaBase):
	pass

class Area(AreaBase):
	areaid: int
	
	class Config:
		orm_mode = True