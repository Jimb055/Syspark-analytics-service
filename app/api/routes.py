from fastapi import APIRouter
from app.services.analytics_service import get_general_statistics
from app.models.statistics import StatisticsResponse

router = APIRouter()

@router.get("/", response_model=StatisticsResponse)
async def get_statistics():
    return await get_general_statistics()
