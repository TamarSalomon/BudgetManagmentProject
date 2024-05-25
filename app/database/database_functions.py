from bson import ObjectId

from app.database.database_connection import my_db

from app.utils import to_json
import json
from bson import json_util



async def get_all(collection_name):
    """
    Retrieves all documents from a specified collection.

    Args:
        collection_name (str): The name of the collection to retrieve documents from.

    Returns:
        list: A list of documents from the collection.
    """
    try:
        cursor = my_db[collection_name].find({})
        results = await cursor.to_list(length=None)
        return to_json(results)
        if not results:
          raise ValueError("users not found")
    except ValueError as ve:
        raise ve
    except Exception as e:
        raise RuntimeError(f"Error retrieving documents from collection {collection_name}: {e}")


async def get_by_id( collection_name,object_id):
    """
      Retrieves a document by its ID from a specified collection in the database.

      Args:
          object_id (any): The ID of the document to retrieve.
          collection_name (str): The name of the collection in the database.

      Returns:
          dict: A dictionary containing the retrieved document.
      """
    try:
        result = await my_db[collection_name].find_one({"id": object_id})
        if not result:
            raise ValueError("document not found")
        return to_json(result)
    except ValueError as ve:
        raise ve
    except Exception as e:
        raise RuntimeError(f"Error cannot get this {object_id} object: {e}")




async def add(collection_name, document):
    """
       Adds a document to a specified collection in the database.

       Args:
           document (dict): The document to be added.
           collection_name (str): The name of the collection in the database.

       Returns:
           dict: A dictionary containing the inserted ID.
       """
    try:
        result = await my_db[collection_name].insert_one(document)
        return {"inserted_id": str(result.inserted_id)}
    except Exception as e:
        raise RuntimeError(f"Error adding document to collection {collection_name}: {e}")

async def login(collection_name, object_name, object_password):
    """
        Logs in a user.

        Args:
            collection_name (str): The name of the collection in the database.
            object_name (str): The username of the user.
            object_password (str): The password of the user.

        Returns:
            list: A list of dictionaries containing user information.
        """
    try:
        all_users = await get_all(collection_name)
        filtered_users = [user for user in all_users if
                          user['user_name'] == object_name and user['password'] == object_password]
        if not filtered_users:
            raise ValueError("User not found")
        return filtered_users
    except ValueError as ve:
        raise ve
    except Exception as e:
        raise RuntimeError(f"Error during login: {e}")



async def update(collection_name,object):
    """
      Updates a document in the specified collection.

      Args:
          document (dict): The updated document.
          collection_name (str): The name of the collection in the database.

      Returns:
          str: A message indicating the success of the update.
      """
    try:
        existing_document = await get_by_id( collection_name,object['id'])
        if existing_document:
            await my_db[collection_name].replace_one({"id": object['id']}, object)
            return f"Document with ID {object['id']} updated successfully."
        else:
            return f"No document found with ID {object['id']}."
    except Exception as e:
        raise RuntimeError(f"Error updating document: {e}")

async def last_id(collection_name):
    try:
        all_collection = await get_all(collection_name)
        if all_collection is None:
            return -1
        max_id = 0
        for item in all_collection:
            if item['id'] > max_id:
                max_id = item['id']
        return max_id
    except Exception as e:
        raise e
