# app/routes/userRouter.py
from fastapi import APIRouter, HTTPException

from app.models.revenue_model import  Revenue

from app.services import revenues_service
import json
from bson import json_util
from app.services import revenues_service
revenues_router = APIRouter()

@revenues_router.post('/create_revenue')
async def create_revenue(new_revenue: Revenue):
    try:
        return await revenues_service.create_revenue(new_revenue)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@revenues_router.get('/{revenue_id}')
async def get_revenue_by_id(revenue_id:int ):
    try:
        return await revenues_service.get_revenue_by_id(revenue_id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
