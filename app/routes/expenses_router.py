from fastapi import APIRouter, HTTPException,Depends
from app.models.expense_model import Expense
from app.services import expenses_service
from app.validition import validition_functions
expense_router = APIRouter()



@expense_router.get('/expenses/{user_id}')
async def get_all_expenses_by_user_id(user_id: int):
    """
        Retrieve all expenses for a specific user.

        Args:
            user_id (int): The ID of the user.

        Returns:
            List[Expense]: A list of expense objects.

        Raises:
            HTTPException: If no expenses are found (400) or any server error occurs (500).
        """
    try:
        return await expenses_service.get_all_expenses_by_user_id(user_id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@expense_router.get('/{expense_id}')
async def get_expense_by_id(expense_id: int):
    """
       Retrieve an expense by its ID.

       Args:
           expense_id (int): The ID of the expense.

       Returns:
           Expense: The expense object corresponding to the given ID.

       Raises:
           HTTPException: If the expense is not found (400) or any server error occurs (500).
       """
    try:
        return await expenses_service.get_expense_by_id(expense_id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))




@expense_router.post('/create_expense_to_user/{user_id}')
async def create_expense(user_id: int, new_expense: Expense):
    """
        Create a new expense for a specific user.

        Args:
            user_id (int): The ID of the user.
            new_expense (Expense): The expense object to be created.

        Returns:
            Expense: The newly created expense object.

        Raises:
            HTTPException: If any server error occurs (500).
        """
    try:
        return await expenses_service.create_expense(user_id, new_expense)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@expense_router.put('/update_expense/{expense_id}')
async def update_expense(expense_id: int, new_expense: Expense):
    """
     Update an existing expense.

     Args:
         expense_id (int): The ID of the expense to be updated.
         new_expense (Expense): The updated expense object.

     Returns:
         Expense: The updated expense object.

     Raises:
         HTTPException: If any server error occurs (500).
     """
    try:
        return await expenses_service.update_expense(expense_id, new_expense)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@expense_router.delete('/delete_expense/{expense_id}')
async def delete_revenue(expense_id: int):
    """
       Delete an expense by its ID.

       Args:
           expense_id (int): The ID of the expense to delete.

       Returns:
           str: A success message indicating the expense was deleted.

       Raises:
           HTTPException: If the expense is not found (400) or any server error occurs (500).
       """
    try:
        return await expenses_service.delete_expense(expense_id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


