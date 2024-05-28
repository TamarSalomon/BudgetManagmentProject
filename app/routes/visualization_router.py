from http.client import HTTPException

from fastapi import APIRouter
from app.services import visualization_service
visualization_router = APIRouter()

@visualization_router.get('/plot_income_expense_per_user')
async def plot_income_expense_per_user():
    try:
        return await visualization_service.plot_income_expense_per_user()
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


