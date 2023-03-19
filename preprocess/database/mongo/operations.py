import config as cf
import constants as cs
from pymongo import MongoClient
from pprint import pprint

def get_database(db_name):
    CONNECTION_STRING = cf.get_configs()["DATABASE"]["CONNECTION"]
    client = MongoClient(CONNECTION_STRING)
    return client[db_name]

def insert_many(insert_list, db, collection_name):
    db[collection_name].insert_many(insert_list)

def insert_one(insert_item, collection_name):
    db[collection_name].insert_one(insert_item)

def query(key_name, value, db, collection_name):
    result = db[collection_name].find({key_name : value})
    return result

def query_count(key_name, value, db, collection_name):
    result = db[collection_name].find({key_name : value,}, {})
    num = 0
    for i in result:
        num += 1
    return num

