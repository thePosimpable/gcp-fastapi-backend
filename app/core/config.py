import pytz
import os
import sys

from typing import Any, Dict, List, Optional, Union
from pydantic import BaseSettings
from dotenv import load_dotenv

# NOTE: __file__ = /gcp-fastapi-backend/app/core/config.py, os.path.dirname(os.path.dirname(os.path.dirname())) = /gcp-fastapi-backend
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

load_dotenv(os.path.join(BASE_DIR, '.env'))

class Settings(BaseSettings):
	POSTGRES_USER: str = os.environ.get('POSTGRES_USER')
	POSTGRES_PASSWORD: str = os.environ.get('POSTGRES_PASSWORD')
	POSTGRES_SERVER: str = os.environ.get('POSTGRES_SERVER')
	POSTGRES_PORT: str = os.environ.get('POSTGRES_PORT')
	POSTGRES_DB: str = os.environ.get('POSTGRES_DB')
	DATABASE_URL: str = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}/{POSTGRES_DB}"
	TIMEZONE: Any = pytz.timezone('Asia/Singapore')
	API_V1_STR: str = "/api/v1"
	
	class Config:
		case_sensitive = True

settings = Settings()