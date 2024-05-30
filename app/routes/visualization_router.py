from fastapi import APIRouter, HTTPException
from app.services import visualization_service
from app.utils import log_function_call

visualization_router = APIRouter()


@visualization_router.get('/plot_revenue_expense_per_user')
@log_function_call
async def plot_revenue_expense_per_user(user_id: int):
    """
    Endpoint to plot a bar chart showing the total revenue and total expense for a specific user in the current month.

    Args:
        user_id (int): The ID of the user.

    Raises:
        HTTPException: If the user with the specified ID is not found or any other error occurs.

    Returns:
        None: Displays a bar chart showing total revenue and expense for the specified user in the current month.
    """
    try:
        return await visualization_service.plot_revenue_expense_per_user(user_id)
    except ValueError as e:
        print(f"ValueError: {e}")
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        print(f"Exception: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@visualization_router.get('/plot_revenue_expense_over_time')
@log_function_call
async def plot_revenue_expense_over_time(user_id: int):
    """
    Endpoint to plot a line chart showing the total revenue and total expense over time for a specific user.

    Args:
        user_id (int): The ID of the user.

    Raises:
        HTTPException: If the user with the specified ID is not found or any other error occurs.

    Returns:
        None: Displays a line chart showing total revenue and expense over time for the specified user.
    """
    try:
        return await visualization_service.plot_revenue_expense_over_time(user_id)
    except ValueError as e:
        print(f"ValueError: {e}")
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        print(f"Exception: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@visualization_router.get('/plot_pie_chart')
@log_function_call
async def plot_pie_chart(user_id: int):
    """
    Endpoint to plot a pie chart showing the distribution of expenses and revenues for a specific user in the current month.

    Args:
        user_id (int): The ID of the user.

    Raises:
        HTTPException: If the user with the specified ID is not found or any other error occurs.

    Returns:
        None: Displays a pie chart showing the distribution of expenses and revenues for the specified user in the current month.
    """
    try:
        return await visualization_service.plot_pie_chart(user_id)
    except ValueError as e:
        print(f"ValueError: {e}")
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        print(f"Exception: {e}")
        raise HTTPException(status_code=500, detail=str(e))
