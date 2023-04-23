import datetime

from sqlalchemy import (
	Boolean,
	Column,
	ForeignKey,
	Integer,
	String,
	SmallInteger,
	Numeric,
	Date,
	DateTime,
	Float,
)

from sqlalchemy.orm import relationship, synonym
from sqlalchemy.sql import func

from app.db.session import Base

class Book(Base):
	__tablename__ = "books"

	bookId  = Column(Integer, primary_key = True, index = True,)
	title = Column(String)
	rating = Column(Float)

	createdAt = Column(DateTime(timezone = True), server_default = func.now())
	updatedAt = Column(DateTime(timezone = True), server_default = func.now(), onupdate = func.now())

	book_id = synonym('bookId')
	created_at = synonym('createdAt')
	updated_at = synonym('updatedAt')

	# author_id = Column(Integer, ForeignKey('author.id'))