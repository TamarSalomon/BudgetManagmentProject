from fastapi import APIRouter, Depends, HTTPException
from app.models.user_model import User
from app.services import users_service
from app.validition import validition_functions

user_router = APIRouter()


@user_router.get('/users')
async def get_all_users():
    """
       Retrieve all users from the database.

       Returns:
           List[User]: A list of user objects.

       Raises:
           HTTPException: If no users are found (404) or any server error occurs (500).
       """
    try:
        return await users_service.get_all_users()
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@user_router.get('/users/{user_id}')
async def get_user_by_id(user_id: int):
    """
       Retrieve a user by their ID.

       Args:
           user_id (int): The ID of the user to retrieve.

       Returns:
           User: The user object corresponding to the given ID.

       Raises:
           HTTPException: If the user is not found (404) or any server error occurs (500).
       """
    try:
        return await users_service.get_user_by_id(user_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@user_router.post('')
async def add_user(new_user: User):
    """
    Create a new user.

    Args:
        new_user (User): The user object to be created.

    Returns:
     dict: A dictionary containing the inserted ID as a string.

    Raises:
        HTTPException: If any server error occurs (500).
    """
    try:
        return await users_service.create_user(new_user)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@user_router.put('/{user_id}')
async def update_user(user_id: int, new_user: User):

        """
          Update an existing user.

          Args:
              user_id (int): The ID of the user to be updated.
              new_user (User): The updated user object.

          Returns:
            str: A success message indicating the user was updated.

          Raises:
              HTTPException: If any server error occurs (500).
          """
        try:
            return await users_service.update_user(user_id, new_user)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))



@user_router.delete('/{user_id}')
async def delete_user(user_id: int):
    """
       Delete a user by their ID.

       Args:
           user_id (int): The ID of the user to delete.

       Returns:
            str: A success message indicating the user was deleted.

       Raises:
           HTTPException: If the user is not found (400) or any server error occurs (500).
       """
    try:
        return await users_service.delete_user(user_id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))



@user_router.post('/login')
async def login_user(user_name: str, user_password: str):
    """
       Authenticate a user with their username and password.

       Args:
           user_name (str): The username of the user.
           user_password (str): The password of the user.

       Returns:
           List[User]: The authenticated user object.

       Raises:
           HTTPException: If the user is not found or the password is invalid (400) or any server error occurs (500).
       """
    try:
        return await users_service.login_user(user_name, user_password)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
