from app.database import database_functions
from app.models.revenue_model import Revenue
from datetime import datetime
from app.services.users_service import update_user
from app.models.user_model import User


async def get_revenue_by_id(revenue_id: int):
    """
    Retrieves revenue details by its ID.

    Args:
        revenue_id (int): The ID of the revenue to retrieve.

    Returns:
        dict: A dictionary containing the revenue details.

    Raises:
        ValueError: If the revenue is not found.
        Exception: For any other unexpected error.
    """
    try:
        revenue = await database_functions.get_by_id(revenue_id, "revenues")
        if revenue is None:
            raise ValueError("Revenue not found")
        return revenue
    except ValueError as ve:
        raise ve
    except Exception as e:
        raise e


async def get_all_revenues_by_user_id(user_id: int):
    """
    Retrieves all revenues for a specific user by their ID.

    Args:
        user_id (int): The ID of the user.

    Returns:
        List[dict]: A list containing dictionaries of revenue details.

    Raises:
        ValueError: If no revenues are found for the user.
        Exception: For any other unexpected error.
    """
    try:
        all_revenues = await database_functions.get_all_by_user_id(user_id, "revenues")
        if not all_revenues:
            raise ValueError("Revenues not found")
        return all_revenues
    except ValueError as ve:
        raise ve
    except Exception as e:
        raise e


async def create_revenue(user_id, new_revenue: Revenue):
    """
    Creates a new revenue for a specific user.

    Args:
        user_id (int): The ID of the user.
        new_revenue (Revenue): The revenue details.

    Returns:
        str: A message indicating the success of the operation.

    Raises:
        ValueError: If the user is not found.
        Exception: For any other unexpected error.
    """
    try:
        new_revenue.id = await database_functions.last_id(collection_name="revenues") + 1
        new_revenue.user_id = user_id
        user = await database_functions.get_by_id(user_id, "users")
        if user is None:
            raise ValueError("User not found")
        user['balance'] += new_revenue.total_revenue
        await database_functions.update(user, "users")

        new_revenue_dict = new_revenue.dict()
        return await database_functions.add(new_revenue_dict, "revenues")
    except ValueError as ve:
        raise ve
    except Exception as e:
        raise e


async def update_revenue(revenue_id: int, new_revenue: Revenue):
    """
    Updates an existing revenue.

    Args:
        revenue_id (int): The ID of the revenue to update.
        new_revenue (Revenue): The updated revenue details.

    Returns:
        str: A message indicating the success of the update.

    Raises:
        Exception: For any unexpected error.
    """
    try:
        existing_revenue = await get_revenue_by_id(revenue_id)
        last_user_id = existing_revenue['user_id']
        last_total_revenue = existing_revenue['total_revenue']

        user_data = await database_functions.get_by_id(last_user_id, "users")
        user = User(**user_data)
        user.balance -= last_total_revenue
        await update_user(last_user_id, user, True)

        new_user_data = await database_functions.get_by_id(new_revenue.user_id, "users")
        new_user = User(**new_user_data)
        new_user.balance += new_revenue.total_revenue
        await update_user(new_revenue.user_id, new_user, True)

        new_revenue.id = revenue_id
        new_revenue.date = datetime.now()
        updated_revenue = new_revenue.dict()
        return await database_functions.update(updated_revenue, collection_name="revenues")
    except Exception as e:
        raise e


async def delete_revenue(revenue_id):
    """
    Deletes an existing revenue.

    Args:
        revenue_id (int): The ID of the revenue to delete.

    Returns:
        str: A message indicating the success of the deletion.

    Raises:
        ValueError: If the revenue is not found.
        Exception: For any other unexpected error.
    """
    try:
        revenue = await get_revenue_by_id(revenue_id)
        user_data = await database_functions.get_by_id(revenue['user_id'],"users")
        user = User(**user_data)
        user.balance -= revenue['total_revenue']
        await update_user(revenue['user_id'], user, True)
        return await database_functions.delete(revenue['id'],"revenues")
    except ValueError as ve:
        raise ve
    except Exception as e:
        raise e