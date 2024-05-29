import re



def is_valid_name(name: str) :
    """
      Validate if the string is a valid name consisting of only alphabetic characters.
      Args:
          name (str): The name to validate.
      Returns:
          str: The validated name.
      Raises:
          ValueError: If the name is not in the correct format.
      """
    if re.match(r'^[a-zA-Z]+$', name):
        return name
    else:
        raise ValueError('Invalid name format')



def is_valid_password(password: str):
    """
       Validate if the string is a valid password.
       Args:
           password (str): The password to validate.
       Returns:
           str: The validated password.
       Raises:
           ValueError: If the password is not in the correct format.
       """
    if len(password) < 8:
        raise ValueError('Password must be at least 8 characters long')
    if not re.search(r'[A-Z]', password):
        raise ValueError('Password must contain at least one uppercase letter')
    if not re.search(r'[a-z]', password):
        raise ValueError(status_code=400, detail='Password must contain at least one lowercase letter')
    if not re.search(r'[0-9]', password):
        raise ValueError(status_code=400, detail='Password must contain at least one digit')
    return password

def is_valid_email(email: str) :
    """
       Validate if the string is a valid email address.
       Args:
           email (str): The email address to validate.
       Returns:
           str: The validated email address.
       Raises:
           ValueError: If the email address is not in the correct format.
       """

    if not re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email):
        raise ValueError('Invalid email address format')
    return email

def is_valid_phone(phone: str) :
    """
       Validate if the string is a valid phone number.
       Args:
           phone (str): The phone number to validate.
       Returns:
           str: The validated phone number.
       Raises:
           ValueError: If the phone number is not in the correct format.
       """
    if len(phone) < 9 or len(phone) > 10:
        raise ValueError('Phone number must be 9 or 10 digits long')
    return phone

def is_valid_amount(amount: float) :
    """
    Validate if the amount is a positive number.
    Args:
        amount (float): The amount to validate.
    Returns:
        float: The validated amount.
    Raises:
        ValueError: If the amount is not positive.
    """
    if amount <= 0:
        raise ValueError('Amount must be a positive number')
    return amount




