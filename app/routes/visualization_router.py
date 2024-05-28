from fastapi import APIRouter, HTTPException
from app.services import visualization_service

visualization_router = APIRouter()


@visualization_router.get('/plot_revenue_expense_per_user')
async def plot_revenue_expense_per_user():
    try:
        return await visualization_service.plot_revenue_expense_per_user()
    except ValueError as e:
        print(f"ValueError: {e}")
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        print(f"Exception: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@visualization_router.get('/plot_revenue_expense_over_time')
async def plot_revenue_expense_over_time():
    try:
        return await visualization_service.plot_revenue_expense_over_time()
    except ValueError as e:
        print(f"ValueError: {e}")
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        print(f"Exception: {e}")
        raise HTTPException(status_code=500, detail=str(e))





@visualization_router.get('/plot_financial_management_per_user')
async def plot_financial_management_per_user_endpoint():
    try:
        return await visualization_service.plot_financial_management_per_user()
    except ValueError as e:
        print(f"ValueError: {e}")
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        print(f"Exception: {e}")
        raise HTTPException(status_code=500, detail=str(e))