from app.database.database_connection import my_db
from app.utils import to_json


async def get_all(collection_name):
    """
    Retrieves all documents from a specified collection in the database.

    Args:
        collection_name (str): The name of the collection in the database.

    Returns:
        list: A list containing dictionaries of retrieved documents.
    """
    try:
        cursor = my_db[collection_name].find({})
        results = await cursor.to_list(length=None)
        return to_json(results)
    except Exception as e:
        raise RuntimeError(f"Error retrieving documents from collection {collection_name}: {e}")


async def get_by_id(collection_name,object_id):
    """
    Retrieves a document by its ID from a specified collection in the database.

    Args:
        object_id (any): The ID of the document to retrieve.
        collection_name (str): The name of the collection in the database.

    Returns:
        dict: A dictionary containing the retrieved document.
    """
    try:
        element = await my_db[collection_name].find_one({"id": object_id})
        if element is None:
            raise ValueError("Element not found")
        return to_json(element)
    except Exception as e:
        raise RuntimeError(f"Error retrieving document: {e}")


async def add( collection_name,document):
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


async def update(collection_name,document):
    """
    Updates a document in the specified collection.

    Args:
        document (dict): The updated document.
        collection_name (str): The name of the collection in the database.

    Returns:
        str: A message indicating the success of the update.
    """
    try:
        existing_document = await get_by_id( collection_name,document['id'])
        if existing_document:
            new_document = {key: value for key, value in document.items() if key != '_id'}
            await my_db[collection_name].update_one({"id": document['id']}, {"$set": new_document})
            return f"Document with ID {document['id']} updated successfully."
        else:
            return f"No document found with ID {document['id']}."
    except Exception as e:
        raise RuntimeError(f"Error updating document: {e}")





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


async def get_all_by_user_id(collection_name,user_id):
    """
    Retrieves all items belonging to a specific user ID from a specified collection in the database.

    Args:
        user_id (any): The ID of the user.
        collection_name (str): The name of the collection in the database.

    Returns:
        list: A list containing dictionaries of retrieved items.
    """
    try:
        all_items = await my_db[collection_name].find({"user_id": user_id}).to_list(length=None)
        for item in all_items:
            item["_id"] = str(item["_id"])
        return all_items
    except Exception as e:
        raise RuntimeError(f"Error retrieving items by user ID: {e}")


async def delete( collection_name,document_id):
    """
    Deletes a document from a specified collection in the database by its ID.

    Args:
        document_id (any): The ID of the document to delete.
        collection_name (str): The name of the collection in the database.

    Returns:
        str: A message indicating the success of the deletion.

    Raises:
        RuntimeError: If there is an error during the deletion process.
    """
    try:
        result = await my_db[collection_name].delete_one({"id": document_id})
        print(result)
        if result is not None:
            return f"Document with ID {document_id} deleted successfully."
        else:
            return f"No document found with ID {document_id}."
    except Exception as e:
        raise RuntimeError(f"Error deleting document: {e}")