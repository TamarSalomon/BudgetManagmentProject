from app import utils
from app.database import database_functions
from app.models.revenue_model import Revenue
from datetime import datetime
from app.models.user_model import User

async def get_all_revenues_by_user_id(user_id: int):
    """
       Retrieve all revenues for a specific user.
       Args:
           user_id (int): The ID of the user.
       Returns:
           List[Revenue]: A list of revenues for the user.
       Raises:
           ValueError: If no revenues are found for the user.
           Exception: For any other unexpected errors.
       """
    try:
        all_revenues = await database_functions.get_all_by_user_id("revenues",user_id)
        if not all_revenues:
            raise ValueError("Revenues not found")
        return all_revenues
    except ValueError as ve:
        raise ve
    except Exception as e:
        raise e


async def get_revenue_by_id(revenue_id: int):
    """
        Retrieve a revenue by its ID.
        Args:
            revenue_id (int): The ID of the revenue to retrieve.
        Returns:
            Revenue: The revenue object if found.
        Raises:
            ValueError: If the revenue is not found.
            Exception: For any other unexpected errors.
        """
    try:
        revenue = await database_functions.get_by_id("revenues",revenue_id)
        if revenue is None:
            raise ValueError("Revenue not found")
        return revenue
    except ValueError as ve:
        raise ve
    except Exception as e:
        raise e




async def create_revenue(user_id, new_revenue: Revenue):
    """
        Create a new revenue entry for a user.
        Args:
            user_id (int): The ID of the user.
            new_revenue (Revenue): The revenue object containing revenue details.
        Returns:
          dict: A dictionary containing the inserted ID as a string.
        Raises:
            ValueError: If the user is not found.
            Exception: For any unexpected errors during revenue creation.
        """
    try:
        new_revenue.id = await utils.last_id("revenues") + 1
        new_revenue.user_id = user_id
        user = await database_functions.get_by_id("users",user_id)
        if user is None:
            raise ValueError("User not found")
        user['balance'] += new_revenue.total_revenue
        await database_functions.update("users",user)

        # Convert Revenue object to dictionary before adding to database
        new_revenue_dict = new_revenue.dict()
        return await database_functions.add("revenues",new_revenue_dict)
    except ValueError as ve:
        raise ve
    except Exception as e:
        raise e


async def update_revenue(revenue_id: int, new_revenue: Revenue):
    """
      Update an existing revenue entry.
      Args:
          revenue_id (int): The ID of the revenue to update.
          new_revenue (Revenue): The revenue object containing updated details.
      Returns:
           str: Success message indicating the revenue was updated.
      Raises:
          Exception: For any unexpected errors during revenue update.
      """
    try:
        existing_revenue = await get_revenue_by_id(revenue_id)
        last_user_id = existing_revenue['user_id']
        last_total_revenue = existing_revenue['total_revenue']

        user_data = await database_functions.get_by_id("users", last_user_id)
        user = User(**user_data)
        user.balance -= last_total_revenue
        await database_functions.update("users", user.dict())

        new_user_data = await database_functions.get_by_id("users", new_revenue.user_id)
        new_user = User(**new_user_data)
        new_user.balance += new_revenue.total_revenue
        await database_functions.update("users", new_user.dict())

        new_revenue.id = revenue_id
        new_revenue.date = datetime.now()
        updated_revenue = new_revenue.dict()
        return await database_functions.update("revenues", updated_revenue)
    except Exception as e:
        raise e


async def delete_revenue(revenue_id):
    """
       Delete a revenue entry and update the user's balance accordingly.
       Args:
           revenue_id (int): The ID of the revenue to delete.
       Returns:
           str: Success message indicating the revenue was deleted.
       Raises:
           ValueError: If the revenue is not found.
           Exception: For any other unexpected errors.
       """
    try:
        revenue = await get_revenue_by_id(revenue_id)
        if not revenue:
            raise ValueError(f"Revenue with ID {revenue_id} not found.")

        user_data = await database_functions.get_by_id("users", revenue['user_id'])
        user = User(**user_data)
        user.balance -= revenue['total_revenue']
        await database_functions.update("users", user.dict())

        await database_functions.delete("revenues", revenue['id'])
        return f"Revenue with ID {revenue_id} deleted successfully."
    except ValueError as ve:
        raise ve
    except Exception as e:
        raise e
