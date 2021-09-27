from fastapi import APIRouter
from api.endpoints.login import router

api_router = APIRouter()

api_router.include_router(router, tags=['LOGIN'])
