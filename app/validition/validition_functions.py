from fastapi import HTTPException
from app.models.user_model import User
from app.database.database_functions import get_by_id, get_all
import re
from app.database import database_functions

def is_valid_id(id: str) -> bool:
    """
       Validate if the string is a valid integer ID.
       Args:
           id (str): The ID to validate.
       Returns:
           bool: True if the ID is valid, False otherwise.
       Raises:
           HTTPException: If the ID is not in the correct format.
       """
    if not re.match(r'^\d+$', id):
        raise HTTPException(status_code=400, detail='Invalid ID format. Must contain only digits.')
    return True

def is_valid_name(name: str) :
    """
        Validate if the string is a valid name.
        Args:
            name (str): The name to validate.
        Returns:
            bool: True if the name is valid, False otherwise.
        Raises:
            HTTPException: If the name is not in the correct format.
        """
    if re.match(r'^[a-zA-Z]+$', name):
        return True
    else:
        raise HTTPException(status_code=400, detail='Invalid name format')



def is_valid_password(password: str):
    """
    Validate if the string is a valid password.
    Args:
        password (str): The password to validate.
    Returns:
        bool: True if the password is valid, False otherwise.
    Raises:
        HTTPException: If the password is not in the correct format.
    """
    if len(password) < 8:
        raise HTTPException(status_code=400, detail='Password must be at least 8 characters long')
    if not re.search(r'[A-Z]', password):
        raise HTTPException(status_code=400, detail='Password must contain at least one uppercase letter')
    if not re.search(r'[a-z]', password):
        raise HTTPException(status_code=400, detail='Password must contain at least one lowercase letter')
    if not re.search(r'[0-9]', password):
        raise HTTPException(status_code=400, detail='Password must contain at least one digit')
    return True

def is_valid_email(email: str) :
    """
      Validate if the string is a valid email address.
      Args:
          email (str): The email address to validate.
      Returns:
          bool: True if the email address is valid, False otherwise.
      Raises:
          HTTPException: If the email address is not in the correct format.
      """
    if not re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email):
        raise HTTPException(status_code=400, detail='Invalid email address format')
    return True

def is_valid_phone(phone: str) :
    """
    Validate if the string is a valid Israeli phone number (landline or mobile).
    Args:
        phone (str): The Israeli phone number to validate.
    Returns:
        bool: True if the phone number is valid, False otherwise.
    Raises:
        HTTPException: If the phone number is not in the correct format.
    """
    if len(phone) < 9 or len(phone) > 10:
        raise HTTPException(status_code=400, detail='Phone number must be 9 or 10 digits long')
    return True



async def is_valid_expense(user_id: int, expense: int) -> bool:
    """
       Validate if the expense is valid for the given user.
       Args:
           user_id (int): The ID of the user.
           expense (int): The expense amount.
       Returns:
           bool: True if the expense is valid, False otherwise.
       Raises:
           HTTPException: If the user does not have enough balance.
       """
    user = await database_functions.get_by_id("users", user_id)
    if user is not None:
        if expense > user['balance']:
            raise HTTPException(status_code=400, detail='Not Enough Money')
    return True

