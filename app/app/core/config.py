import pytz
from typing import Any, Dict, List, Optional, Union
from pydantic import BaseSettings

class Settings(BaseSettings):
	API_V1_STR: str = "/api/v1"
	MYSQL_SERVER: str = "localhost"
	MYSQL_USER: str = "root"
	MYSQL_PASSWORD: str = "password"
	MYSQL_DB: str = "test_acid"
	SQLALCHEMY_DATABASE_URI: str = "mysql://%s:%s@%s/%s" % (MYSQL_USER, MYSQL_PASSWORD, MYSQL_SERVER, MYSQL_DB)
	TIMEZONE: Any = pytz.timezone('Asia/Singapore')
	PAGINATION_SIZE: int = 100
	PAGINATION_MAXSIZE: int = 184467440737

	class Config:
		case_sensitive = True

settings = Settings()