import asyncio
from bson import ObjectId
from app.database.database_functions import get_all
import logging
from functools import wraps
import os

log_path = os.path.join(os.getcwd(), 'logs', '../tests/log.txt')

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    filename=log_path,
                    filemode='a')

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    filename='log.txt',
                    filemode='a')


def log_function_call(func):
    """
    Decorator that logs the function call details including the function name,
    arguments, keyword arguments, and the result.

    Args:
        func (function): The function to be wrapped by the decorator.

    Returns:
        function: The wrapped function with logging functionality.
    """
    if not callable(func):
        raise ValueError(f"{func} is not callable")

    @wraps(func)
    async def async_wrapper(*args, **kwargs):
        logging.info(
            f"Calling async function '{func.__name__}' with arguments {args} and keyword arguments {kwargs}")
        result = await func(*args, **kwargs)
        logging.info(f"Async function '{func.__name__}' returned {result}")
        return result

    @wraps(func)
    def sync_wrapper(*args, **kwargs):
        logging.info(
            f"Calling function '{func.__name__}' with arguments {args} and keyword arguments {kwargs}")
        result = func(*args, **kwargs)
        logging.info(f"Function '{func.__name__}' returned {result}")
        return result

    if asyncio.iscoroutinefunction(func):
        return async_wrapper
    else:
        return sync_wrapper


def to_json(data):
    if isinstance(data, list):
        return [to_json(item) for item in data]
    if isinstance(data, dict):
        return {key: to_json(value) for key, value in data.items()}
    if isinstance(data, ObjectId):
        return str(data)
    return data


async def last_id(collection_name):
    """
    Retrieves the last ID from a specified collection in the database.

    Args:
        collection_name (str): The name of the collection in the database.

    Returns:
        int: The last ID found in the collection.
    """
    try:
        all_collection = await get_all(collection_name)
        if not all_collection:
            return -1
        max_id = max(item.get('id', 0) for item in all_collection)
        return max_id
    except Exception as e:
        raise RuntimeError(f"Error retrieving last ID: {e}")
