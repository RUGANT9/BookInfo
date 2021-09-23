from fastapi import APIRouter
from endpoints.login import router

api_router = APIRouter()

api_router.include_router(router, tags=['LOGIN'])
