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

class Entry(Base):
	__tablename__ = "entries"

	entryId = Column(Integer, primary_key = True, index = True,)
	title = Column(String)
	description = Column(String)
	startDate = Column(Date)
	endDate = Column(Date)
	color = Column(String)
	icon = Column(String)

	createdAt = Column(DateTime(timezone = True), server_default = func.now())
	updatedAt = Column(DateTime(timezone = True), server_default = func.now(), onupdate = func.now())

	entry_id = synonym('entryId')
	start_date = synonym('startDate')
	end_date = synonym('endDate')
	created_at = synonym('createdAt')
	updated_at = synonym('updatedAt')