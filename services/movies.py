#!/usr/bin/python3
import json
import os
from services import root_dir, nice_json
from database import movies_db
from flask import Flask
from werkzeug.exceptions import NotFound

app = Flask(__name__)


@app.route("/", methods=['GET'])
def hello():
    return nice_json({
        "uri": "/",
        "subresource_uris": {
            "movies": "/movies",
            "movie": "/movies/<id>"
        }
    })

@app.route("/movies/<movieid>", methods=['GET'])
def movie_info(movieid):
    movies = movies_db.MoviesDB().get_movies()
    
    for movie in movies:
        if movie['id'] == movieid:
            result = movie
            result['uri'] = '/movies/{}'.format(movieid)
    
            return nice_json(result)
    
    raise NotFound


@app.route("/movies", methods=['GET'])
def movie_record():
    movies = movies_db.MoviesDB().get_movies()
    return nice_json(movies)


if __name__ == "__main__":
    port = int(os.getenv('PORT', '5001'))
    host = os.getenv('HOST', 'localhost')

    app.run(host=host, port=port, debug=True)

