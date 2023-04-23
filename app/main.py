from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from app.api.api_v1.api import api_router
from app.core.config import settings

app = FastAPI()

app.add_middleware(
	CORSMiddleware,
	allow_origins = ['*'],
	allow_credentials = True,
	allow_methods = ['*'],
	allow_headers = ['*']
)

app.include_router(api_router, prefix = settings.API_V1_STR)
# START SERVER: uvicorn app.main:app --reload