from motor.motor_asyncio import AsyncIOMotorClient
import os

"""Setting MongoDB connection details from environment variables with default values if they are not set"""
mongo_host = os.getenv('MONGO_HOST', 'localhost')
mongo_port = os.getenv('MONGO_PORT', '27017')
mongo_db = os.getenv('MONGO_DB', 'BudgetManagment')

"""Creating a connection to MongoDB using AsyncIOMotorClient"""
client = AsyncIOMotorClient(f'mongodb://{mongo_host}:{mongo_port}')
my_db = client[mongo_db]

"""Defining collections for use in the project"""
users = my_db['users']
expenses = my_db['expenses']
revenues = my_db['revenues']
