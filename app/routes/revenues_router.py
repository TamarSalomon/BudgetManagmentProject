from fastapi import APIRouter, HTTPException
from app.models.revenue_model import Revenue
from app.services import revenues_service
from app.utils import log_function_call

revenue_router = APIRouter()


@revenue_router.get('/user/{user_id}')
@log_function_call
async def get_all_revenues_by_user_id(user_id: int):
    """
      Retrieve all revenues for a specific user.

      Args:
          user_id (int): The ID of the user.

      Returns:
          List[Revenue]: A list of revenue objects.

      Raises:
          HTTPException: If no revenues are found (400) or any server error occurs (500).
      """
    try:
        return await revenues_service.get_all_revenues_by_user_id(user_id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@revenue_router.get('/{revenue_id}')
@log_function_call
async def get_revenue_by_id(revenue_id: int):
    """
      Retrieve a revenue by ID.

      Args:
          revenue_id (int): The ID of the revenue.

      Returns:
          Revenue: The revenue object corresponding to the given ID.

      Raises:
          HTTPException: If the revenue is not found (400) or any server error occurs (500).
      """
    try:
        return await revenues_service.get_revenue_by_id(revenue_id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@revenue_router.post('/create_revenue_to_user/{user_id}')
@log_function_call
async def add_revenue(user_id: int, new_revenue: Revenue):
    """
       Create a new revenue for a specific user.

       Args:
           user_id (int): The ID of the user.
           new_revenue (Revenue): The revenue object to be created.

       Returns:
           dict: A dictionary containing the inserted ID as a string.


       Raises:
           HTTPException: If any server error occurs (500).
       """
    try:
        return await revenues_service.create_revenue(user_id, new_revenue)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@revenue_router.put('/update_revenue/{revenue_id}')
@log_function_call
async def update_revenue(revenue_id: int, new_revenue: Revenue):
    """
       Update an existing revenue.

       Args:
           revenue_id (int): The ID of the revenue to be updated.
           new_revenue (Revenue): The updated revenue object.

       Returns:
           str: A success message indicating the revenue was updated.

       Raises:
           HTTPException: If any server error occurs (500).
       """
    try:
        return await revenues_service.update_revenue(revenue_id, new_revenue)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@revenue_router.delete('/delete_revenue/{revenue_id}')
@log_function_call
async def delete_revenue(revenue_id: int):
    """
       Delete a revenue by its ID.

       Args:
           revenue_id (int): The ID of the revenue to delete.

       Returns:
           str: A success message indicating the revenue was deleted.

       Raises:
           HTTPException: If the revenue is not found (400) or any server error occurs (500).
       """
    try:
        return await revenues_service.delete_revenue(revenue_id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
