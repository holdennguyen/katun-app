from fastapi import APIRouter
from app.crawl import crawl_text_tiki

from . import login, users

api_router = APIRouter()
api_router.include_router(login.router, prefix="/login", tags=["login"])
api_router.include_router(users.router, prefix="/users", tags=["users"])


@api_router.get("/")
async def root():
    return {"message": "Backend API for FARM-docker operational !"}


@api_router.post("/{full_path:path}")
async def get_summary(full_path: str):
    text = crawl_text_tiki(full_path)
    # openAPI(text)
    return {"message": text}
