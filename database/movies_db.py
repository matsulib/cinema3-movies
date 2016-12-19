#!/usr/bin/python3
import os
from pymongo import MongoClient
from urllib.parse import urlsplit

class MoviesDB():

    def __init__(self):
        url = os.getenv('MONGODB_URI', 'mongodb://localhost:27017/movies')
        db_name = urlsplit(url).path[1:]
        self.col = MongoClient(url)[db_name]['movies']

    def get_movies(self):
        return list(self.col.find({}, {'_id':False}))
