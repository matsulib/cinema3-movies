import json
import unittest
from copy import deepcopy

from services import movies

class TestMoviesService(unittest.TestCase):

    def setUp(self):
        self.app = movies.app.test_client()
        self.name = 'movies'

    def test_index(self):
        ''' Test /'''
        reply = self.app.get('/')
        actual_reply = json.loads(reply.get_data(True))
        self.assertEqual(actual_reply, {
            'subresource_uris': {
                'movie': '/movies/<id>', 'movies': '/movies'
                },
             'uri': '/'
             })

    def test_movie_records(self):
        ''' Test /movies'''
        reply = self.app.get('{}'.format(self.name))
        actual_reply = json.loads(reply.get_data(True))
        self.assertEqual(actual_reply, GOOD_RESPONSES)

    def test_all_movie_info(self):
        ''' Test /movies/<movieid> for all known movies'''
        for expected in deepcopy(GOOD_RESPONSES):
            movieid = expected['id']
            expected['uri'] = '/movies/{}'.format(movieid)
            reply = self.app.get('{}/{}'.format(self.name, movieid))
            actual_reply = json.loads(reply.get_data(True))
            self.assertEqual(set(actual_reply), set(expected))

    def test_not_found(self):
        invalid_movie_id = 'b18f'
        actual_reply = self.app.get('{}/{}'.format(self.name, invalid_movie_id))
        self.assertEqual(actual_reply.status_code, 404,
                    'Got {} but expected 404'.format(
                        actual_reply.status_code))


GOOD_RESPONSES = [
  {
    'title': 'The Good Dinosaur',
    'rating': 7.4,
    'director': 'Peter Sohn',
    'id': '720d006c-3a57-4b6a-b18f-9b713b073f3c'
  },
  {
    'title': 'The Martian',
    'rating': 8.2,
    'director': 'Ridley Scott',
    'id': 'a8034f44-aee4-44cf-b32c-74cf452aaaae'
  },
  {
    'title': 'The Night Before',
    'rating': 7.4,
    'director': 'Jonathan Levine',
    'id': '96798c08-d19b-4986-a05d-7da856efb697'
  },
  {
    'title': 'Creed',
    'rating': 8.8,
    'director': 'Ryan Coogler',
    'id': '267eedb8-0f5d-42d5-8f43-72426b9fb3e6'
  },
  {
    'title': 'Victor Frankenstein',
    'rating': 6.4,
    'director': 'Paul McGuigan',
    'id': '7daf7208-be4d-4944-a3ae-c1c2f516f3e6'
  },
  {
    'title': 'The Danish Girl',
    'rating': 5.3,
    'director': 'Tom Hooper',
    'id': '276c79ec-a26a-40a6-b3d3-fb242a5947b6'
  },
  {
    'title': 'Spectre',
    'rating': 7.1,
    'director': 'Sam Mendes',
    'id': '39ab85e5-5e8e-4dc5-afea-65dc368bd7ab'
  }
]

if __name__ == '__main__':
    unittest.main()
