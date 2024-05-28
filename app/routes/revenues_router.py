from fastapi import APIRouter, HTTPException
from app.models.revenue_model import Revenue
from app.services import revenues_service

revenue_router = APIRouter()


@revenue_router.get('/{revenue_id}')
async def get_revenue_by_id(revenue_id: int):
    """
    Retrieves a revenue by its ID.

    Args:
        revenue_id (int): The ID of the revenue to retrieve.

    Returns:
        dict: The revenue object if found.

    Raises:
        HTTPException: Returns a 400 error if the provided revenue ID is invalid. Returns a 500 error for any other exceptions.
    """
    try:
        return await revenues_service.get_revenue_by_id(revenue_id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@revenue_router.get('/user/{user_id}')
async def get_all_revenues_by_user_id(user_id: int):
    """
    Retrieves all revenues associated with a specific user.

    Args:
        user_id (int): The ID of the user whose revenues to retrieve.

    Returns:
        List[dict]: A list of revenue objects associated with the user.

    Raises:
        HTTPException: Returns a 400 error if the provided user ID is invalid. Returns a 500 error for any other exceptions.
    """
    try:
        return await revenues_service.get_all_revenues_by_user_id(user_id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@revenue_router.post('/create_revenue_to_user/{user_id}')
async def create_revenue(user_id: int, new_revenue: Revenue):
    """
    Creates a new revenue entry for a specific user.

    Args:
        user_id (int): The ID of the user for whom the revenue is being created.
        new_revenue (Revenue): The revenue object containing the details of the new revenue.

    Returns:
        dict: The created revenue object.

    Raises:
        HTTPException: Returns a 400 error if there are issues with the provided data. Returns a 500 error for any other exceptions.
    """
    try:
        return await revenues_service.create_revenue(user_id, new_revenue)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@revenue_router.put('/update revenue/{revenue_id}')
async def update_revenue(revenue_id: int, new_revenue: Revenue):
    """
    Updates an existing revenue entry.

    Args:
        revenue_id (int): The ID of the revenue to update.
        new_revenue (Revenue): The updated revenue object.

    Returns:
        dict: The updated revenue object.

    Raises:
        HTTPException: Returns a 400 error if there are issues with the provided data or if the revenue ID is invalid. Returns a 500 error for any other exceptions.
    """
    try:
        return await revenues_service.update_revenue(revenue_id, new_revenue)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@revenue_router.delete('/delete revenue/{revenue_id}')
async def delete_revenue(revenue_id: int):
    """
    Deletes an existing revenue entry.

    Args:
        revenue_id (int): The ID of the revenue to delete.

    Returns:
        str: A message indicating the success of the deletion.

    Raises:
        HTTPException: Returns a 400 error if the provided revenue ID is invalid. Returns a 500 error for any other exceptions.
    """
    try:
        return await revenues_service.delete_revenue(revenue_id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))