from fastapi import APIRouter

from app.api.api_v1.endpoints import testbase

api_router = APIRouter()
api_router.include_router(testbase.router, prefix="/testbase", tags=["base"])