__author__ = "Frank Kwizera"

from typing import List, Dict
from flask import request, jsonify, session, Flask
from src.server_routes.server_routes import AlbumPhotosEndpoints
from src.get_flask_app import get_flask_app

class AlbumPhotosBackend:
    def __init__(self):
        flask_app: Flask = get_flask_app()
        self.map_endpoints(flask_app=flask_app)

    def map_endpoints(self, flask_app: Flask):
        flask_app.add_url_rule(
            AlbumPhotosEndpoints.GET_ALBUM_PHOTOS + "/<album_id>",
            endpoint="get_album_photos", view_func=self.get_album_photos, methods=['GET'])

    def get_album_photos(self, album_id: str):
        return jsonify({'album_id': album_id})