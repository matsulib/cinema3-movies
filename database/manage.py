import os
import sys
import json
from urllib.parse import urlsplit
from pymongo import MongoClient

def delete_all(col):
    col.delete_many({})

def insert_data(col, data): 
    col.insert_many(data)


if __name__ == '__main__':
    url = os.getenv('MONGODB_URI', 'mongodb://localhost:27017/movies')
    db_name = urlsplit(url).path[1:]
    col = MongoClient(url)[db_name]['movies']
    
    with open('{}/init.json'.format(os.path.dirname(sys.argv[0])), 'r') as f:
        data = json.load(f)
        
    delete_all(col)
    insert_data(col, data)
