from datetime import date, datetime

from typing import List, Optional
from pydantic import Field

from app.schemas import BaseSchema

class EntryBase(BaseSchema):
	title: str
	description: Optional[str] = Field(default = None)
	start_date: 'date'
	end_date: 'date'
	color: Optional[str] = Field(default = None)
	icon: Optional[str] = Field(default = None)
	created_at: datetime
	updated_at: datetime

class EntryCreate(EntryBase):
	pass

class Entry(EntryBase):
	entry_id: int