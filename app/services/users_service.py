import bcrypt
from app import utils
from app.database import database_functions
from app.models.user_model import User


async def get_all_users():
    """
       Retrieve all users from the database.
       Returns:
           List[User]: A list of all users.
       Raises:
           ValueError: If no users are found.
           Exception: For any other unexpected errors.
       """
    try:
        users = await database_functions.get_all("users")
        if users is None:
            return ValueError('No users found')
        return users
    except ValueError as ve:
        raise ve
    except Exception as e:
        raise e


async def get_user_by_id(user_id):
    """
       Retrieve a user by their ID.
       Args:
           user_id (int): The ID of the user to retrieve.
       Returns:
           User: The user object if found.
       Raises:
           ValueError: If the user is not found.
           Exception: For any other unexpected errors.
       """
    try:
        user = await database_functions.get_by_id("users", user_id)
        if user is None:
            raise ValueError("User not found")
        return user
    except ValueError as ve:
        raise ve
    except Exception as e:
        raise e


async def create_user(new_user: User):
    """
       Create a new user in the database.
       Args:
           new_user (User): The user object containing user details.
       Returns:
          dict: A dictionary containing the inserted ID as a string.
       Raises:
           Exception: For any unexpected errors during user creation.
       """
    try:
        new_user.id = await utils.last_id("users") + 1
        new_user.balance = 0
        hashed_password = bcrypt.hashpw(new_user.password.encode('utf-8'), bcrypt.gensalt())
        new_user.password = hashed_password.decode('utf-8')
        user = new_user.dict()
        return await database_functions.add("users", user)
    except Exception as e:
        raise e


async def update_user(user_id: int, new_user: User):
    """
     Update an existing user's details.
     Args:
         user_id (int): The ID of the user to update.
         new_user (User): The user object containing the updated details.
     Returns:
          str: Success message indicating the user was updated.
     Raises:
         Exception: For any unexpected errors during user update.
     """
    try:
        existing_user = await get_user_by_id(user_id)
        new_user.balance = existing_user['balance']
        hashed_password = bcrypt.hashpw(new_user.password.encode('utf-8'), bcrypt.gensalt())
        new_user.password = hashed_password.decode('utf-8')
        new_user.id = user_id
        user = new_user.dict()
        return await database_functions.update("users", user)
    except Exception as e:
        raise e


async def delete_user(user_id):
    """
      Delete a user and their associated revenues and expenses.
      Args:
          user_id (int): The ID of the user to delete.
      Returns:
          str: Success message indicating the user was deleted.
      Raises:
          ValueError: If the user is not found.
          Exception: For any other unexpected errors.
      """
    try:
        await get_user_by_id(user_id)
        revenues_user = await database_functions.get_all_by_user_id("revenues", user_id)
        expense_user = await database_functions.get_all_by_user_id("expenses", user_id)
        for revenue in revenues_user:
            await database_functions.delete("revenues", revenue['id'])
        for expense in expense_user:
            await database_functions.delete("expenses", expense['id'])
        return await database_functions.delete("users", user_id)
    except ValueError as ve:
        raise ve
    except Exception as e:
        raise e


async def login_user(user_name, user_password):
    """
        Authenticate a user based on their username and password.
        Args:
            user_name (str): The username of the user.
            user_password (str): The password of the user.
        Returns:
            User:user containing the authenticated user.
        Raises:
            ValueError: If the user is not found or the password is invalid.
            Exception: For any unexpected errors during login.
        """
    try:
        all_users = await database_functions.get_all("users")
        if not all_users:
            raise ValueError('List users not found')
        for user in all_users:
            if user['name'] == user_name and bcrypt.checkpw(user_password.encode('utf-8'),
                                                            user['password'].encode('utf-8')):
                return [user]
        raise ValueError("User not found or invalid password")
    except ValueError as ve:
        raise ve
    except Exception as e:
        raise RuntimeError(f"Error during login: {e}")
