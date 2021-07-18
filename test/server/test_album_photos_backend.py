__author__ = "Frank Kwizera"

from src.server.album_photos_backend import AlbumPhotosBackend
from src.server_routes.server_routes import AlbumPhotosEndpoints
from src.server.server_constants import ServerConstants
import unittest
from flask.wrappers import Response
from flask import Flask
from flask.testing import FlaskClient
from src.get_flask_app import get_flask_app
import json
from typing import Dict, List, Union


class AlbumPhotosBackendTest(unittest.TestCase):
    @classmethod
    def setup_class(cls):
        cls.flask_app: Flask = get_flask_app(testing=True)
        cls.flask_test_client: FlaskClient = cls.flask_app.test_client()

        # Initiate the micro server
        cls.album_photos_backend: AlbumPhotosBackend = AlbumPhotosBackend()

    def test_get_album_photos(cls):
        album_id: int = 5
        album_photos_response: Response = \
            cls.flask_test_client.get(AlbumPhotosEndpoints.GET_ALBUM_PHOTOS + '/{0}'.format(album_id))
        
        cls.assertEqual(200, album_photos_response.status_code)
        album_photos_json_response: List[Dict[str, str]] = json.loads(album_photos_response.data)

        all_objs_has_title: bool = all('title' in response for response in album_photos_json_response)
        cls.assertTrue(all_objs_has_title)

        all_objs_has_thumbnailUrl: bool = all('thumbnailUrl' in response for response in album_photos_json_response)
        cls.assertTrue(all_objs_has_thumbnailUrl)
    
    def test_get_album_photos_with_invalid_id(cls):
        album_id: str = 'test'
        album_photos_response: Response = \
            cls.flask_test_client.get(AlbumPhotosEndpoints.GET_ALBUM_PHOTOS + '/{0}'.format(album_id))
        cls.assertEqual(400, album_photos_response.status_code)

        album_photos_json_response: Dict[str, str] = json.loads(album_photos_response.data)
        cls.assertEqual(
            album_photos_json_response[ServerConstants.SERVER_ERROR_MESSAGE_KEY], 
            ServerConstants.REQUIRED_ALBUM_ID)

    @classmethod
    def teardown_class(cls):
        pass

if __name__ == '__main__':
    unittest.main(verbosity=2)