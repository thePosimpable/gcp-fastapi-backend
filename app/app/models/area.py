import datetime

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, SmallInteger, Numeric, Date, DateTime
from sqlalchemy.orm import relationship

from app.db.session import Base

class Area(Base):
	__tablename__ = "areas"

	areaid = Column(Integer, primary_key = True, index = True)
	arearepname = Column(String)
	arealocation = Column(String)
	areadaysallowance = Column(Integer, default = 0)
	created_at = Column(DateTime, default = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
	updated_at = Column(DateTime, default = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), onupdate = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))