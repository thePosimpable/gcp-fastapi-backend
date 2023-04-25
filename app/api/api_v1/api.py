from fastapi import APIRouter

from app.api.api_v1.endpoints import entries

api_router = APIRouter()
api_router.include_router(entries.router, prefix="/entries", tags = ["entries"])