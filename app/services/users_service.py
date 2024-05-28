import bcrypt

from app import utils
from app.database import database_functions
from app.models.user_model import User


async def get_all_users():
    """
    Retrieves all users.

    Returns:
        list: A list containing dictionaries of user information.
    """
    try:
        users = await database_functions.get_all("users")
        print(users)
        if users is None:
            return ValueError('List users not found')
        return users
    except ValueError as ve:
        raise ve
    except Exception as e:
        raise e


async def get_user_by_id(user_id):
    """
    Retrieves a user by their ID.

    Args:
        user_id (int): The ID of the user to retrieve.

    Returns:
        dict: A dictionary containing the user's information.
    """
    try:
        user = await database_functions.get_by_id("users",user_id)
        if user is None:
            raise ValueError("User not found")
        return user
    except ValueError as ve:
        raise ve
    except Exception as e:
        raise e


async def create_user(new_user: User):
    """
    Creates a new user.

    Args:
        new_user (User): The user object to be created.

    Returns:
        dict: A dictionary containing the result of adding the user.
    """
    try:
        hashed_password = bcrypt.hashpw(new_user.password.encode('utf-8'), bcrypt.gensalt())

        new_user.id = await utils.last_id("users") + 1
        new_user.balance = 0
        new_user.password = hashed_password.decode('utf-8')

        user = new_user.dict()
        return await database_functions.add("users",user)
    except Exception as e:
        raise e


async def login_user(user_name, user_password):
    """
    Logs in a user.

    Args:
        user_name (str): The username of the user.
        user_password (str): The password of the user.

    Returns:
        list: A list of dictionaries containing user information.
    """
    try:
        all_users = await database_functions.get_all("users")
        if not all_users:
            return ValueError('List users not found')
        for user in all_users:
            if user['name'] == user_name and bcrypt.checkpw(user_password.encode('utf-8'), user['password'].encode('utf-8')):
                return [user]
        raise ValueError("User not found or invalid password")
    except ValueError as ve:
        raise ve
    except Exception as e:
        raise RuntimeError(f"Error during login: {e}")


async def update_user(user_id: int, new_user: User):
    """
    Updates a user's profile.

    Args:
        user_id (int): The ID of the user to update.
        new_user (User): The updated user object.

    Returns:
        str: A message indicating the success of the update.
        :param user_id:
        :param new_user:
    """
    try:
        existing_user = await get_user_by_id(user_id)
        new_user.balance = existing_user['balance']
        hashed_password = bcrypt.hashpw(new_user.password.encode('utf-8'), bcrypt.gensalt())
        new_user.password = hashed_password.decode('utf-8')
        new_user.id = user_id
        user = new_user.dict()
        return await database_functions.update( "users",user)
    except Exception as e:
        raise e


async def delete_user(user_id):
    """
    Deletes a user from the system along with their associated revenues.

    Args:
        user_id (any): The ID of the user to be deleted.

    Returns:
        dict: A dictionary containing the result of deleting the user.
    """
    try:
        await get_user_by_id(user_id)
        revenues_user = await database_functions.get_all_by_user_id("revenues",user_id)
        expense_user = await database_functions.get_all_by_user_id("expenses",user_id)
        for revenue in revenues_user:
            await database_functions.delete("revenues",revenue['id'])
        for expense in expense_user:
            await database_functions.delete("expenses",expense['id'])
        return await database_functions.delete("users",user_id)
    except ValueError as ve:
        raise ve
    except Exception as e:
        raise e