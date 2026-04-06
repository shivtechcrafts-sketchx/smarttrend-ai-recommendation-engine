from fastapi import APIRouter
from app.services.youtube_service import get_real_trends
from app.db.storage import save_video, get_saved

router = APIRouter()

@router.get("/trends")
def get_trends(category: str = "AI", search: str = ""):
    return get_real_trends(category, search)

@router.post("/save")
def save(video: dict):
    save_video(video)
    return {"msg": "saved"}

@router.get("/saved")
def saved():
    return get_saved()