from fastapi import APIRouter
from app.services.service1 import get_service1_data

router = APIRouter()

@router.get("/service1-data")
async def service1_data():
    data = await get_service1_data()
    return {"service1_data": data}
