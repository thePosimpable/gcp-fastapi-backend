import datetime

from typing import List, Optional

from app.schemas import BaseSchema

class BookBase(BaseSchema):
	title: str
	rating: float
	created_at: datetime.datetime
	updated_at: datetime.datetime

class BookCreate(BookBase):
	pass

class Book(BookBase):
	book_id: int