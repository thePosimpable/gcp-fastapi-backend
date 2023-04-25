import random
from datetime import datetime

from datetime import date, datetime
from typing import List, Optional
from pydantic import Field, validator

from app.schemas import BaseSchema

def generate_random_bgcolor() -> str:
	return random.choice(['blue', 'green', 'orange', 'red', 'teal', 'grey', 'purple'])

class EntryBase(BaseSchema):
	title: str
	description: Optional[str] = Field(default = None)
	start_date: 'date'
	end_date: 'date'
	color: Optional[str] = Field(default_factory = generate_random_bgcolor)
	icon: Optional[str] = Field(default = None)
	created_at: Optional[datetime] = Field(default = datetime.now())
	updated_at: Optional[datetime] = Field(default = datetime.now())

class EntryCreate(EntryBase):
	@validator("color", always = True, pre = True)
	def validate_color(cls, v, field):
		# to set a default value for color = null
		return v or generate_random_bgcolor() 

	@validator("start_date", "end_date", always = True, pre = True)
	def validate_dates(cls, v, field):
		# to set a default value for color = null
		return datetime.strptime(v, '%Y/%m/%d').strftime('%Y-%m-%d')


class Entry(EntryBase):
	entry_id: int

class EntryDisplay(BaseSchema):
	entryId: str = Field(alias = "entryId")
	title: str = Field(alias = "title")
	details: Optional[str] = Field(alias = "description")
	start: 'date' = Field(alias = "startDate")
	end: 'date' = Field(alias = "endDate")
	bgcolor: Optional[str] = Field(alias = "color")
	icon: Optional[str] = Field(alias = "icon")
	createdAt: datetime = Field(alias = "createdAt")
	updatedAt: datetime = Field(alias = "updatedAt")