from pymongo import MongoClient
from motor.motor_asyncio import AsyncIOMotorClient
import os

mongo_host = os.getenv('MONGO_HOST', 'localhost')
mongo_port = os.getenv('MONGO_PORT', '27017')
mongo_db = os.getenv('MONGO_DB', 'BudgetManagment')

client = AsyncIOMotorClient(f'mongodb://{mongo_host}:{mongo_port}')
my_db = client[mongo_db]


users = my_db['users']
expenses = my_db['expenses']
revenues = my_db['revenues']