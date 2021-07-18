__author__ = "Frank Kwizera"

from typing import List, Dict, Union
from flask import jsonify, Flask
from flask.wrappers import Response
from src.server_routes.server_routes import AlbumPhotosEndpoints, JsonPlaceHolderEndpoints
from src.get_flask_app import get_flask_app
import requests

class AlbumPhotosBackend:
    def __init__(self):
        flask_app: Flask = get_flask_app()
        self.map_endpoints(flask_app=flask_app)

    def map_endpoints(self, flask_app: Flask):
        """
        Maps endpoints to related methods.
        """
        flask_app.add_url_rule(
            AlbumPhotosEndpoints.GET_ALBUM_PHOTOS + "/<album_id>",
            endpoint="get_album_photos", view_func=self.get_album_photos, methods=['GET'])

    def get_album_photos(self, album_id: str) -> List[Dict[str, Union[str, int]]]:
        """
        Retrieves album photos of a given album ID.
        Inputs:
            - album_id: ID representing the target album.
        Returns:
            - Jsonfied list of dictionaries containing title and thumbnailUrl.
        """
        json_place_holder_endpoint: str = JsonPlaceHolderEndpoints.ALBUM_PHOTOS.format(album_id)
        request_response: Response = requests.get(json_place_holder_endpoint)
        response_list: List[Dict[str, Union[str, int]]] = \
            list(map(lambda response: {"title": response['title'], "thumbnailUrl": response['thumbnailUrl']}, request_response.json()))
        return jsonify(response_list)