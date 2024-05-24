# app/routes/userRouter.py
from fastapi import APIRouter, HTTPException

from app.models.expense_model import Expense
from app.models.revenue_model import Revenue
from app.models.user_model import User
from app.services import users_service
import json
from bson import json_util
from app.services import revenues_service
expenses_router = APIRouter()

@expenses_router.post('/create')
async def create_expenses(new_revenue: Revenue):
    try:
        return await revenues_service.create_expenses(new_revenue)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))