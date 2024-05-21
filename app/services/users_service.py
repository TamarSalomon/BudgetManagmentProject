# app/services/userService.py
from app.models.user_model import User
from app.database.database_connection import my_db
from app.database import database_functions
async def get_all_users():
    try:
        users = await database_functions.get_all("users")
        return users
    except ValueError as ve:
        raise ValueError(ve)
    except Exception as e:
        raise e
async def get_user_by_id(user_id):
    try:
         return await database_functions.get_by_id("users", user_id)
    except ValueError as ve:
     raise ValueError(ve)
    except Exception as e:
         raise e

async def create_user(user):
    """
    Creates a new user document.
    Args:
        user (dict): The user document to create.

    Returns:
        dict: The inserted document ID.
    """

    try:
        return await database_functions.add_user("users", user)
    except Exception as e:
        raise e