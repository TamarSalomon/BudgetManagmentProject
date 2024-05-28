from fastapi import APIRouter, HTTPException
from app.models.expense_model import Expense
from app.services import expenses_service

expense_router = APIRouter()


@expense_router.get('/{expense_id}')
async def get_expense_by_id(expense_id: int):
    try:
        return await expenses_service.get_expense_by_id(expense_id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@expense_router.get('/user/{user_id}')
async def get_all_expenses_by_user_id(user_id: int):
    try:
        return await expenses_service.get_all_expenses_by_user_id(user_id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@expense_router.post('/create_expense_to_user/{user_id}')
async def create_revenue(user_id: int, new_expense: Expense):
    try:
        return await expenses_service.create_expense(user_id, new_expense)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@expense_router.put('/update expense/{expense_id}')
async def update_revenue(expense_id: int, new_expense: Expense):
    try:
        return await expenses_service.update_expense(expense_id, new_expense)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@expense_router.delete('/delete expense/{expense_id}')
async def delete_revenue(expense_id: int):
    try:
        return await expenses_service.delete_expense(expense_id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


