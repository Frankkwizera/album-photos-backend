__author__ = "Frank Kwizera"

from flask import Flask
from src.get_flask_app import get_flask_app
from src.server.album_photos_backend import AlbumPhotosBackend


class AlbumServerRunner:
    def __init__(self):
        self.debug: bool = True
        self.flask_app: Flask = get_flask_app()

    def attach_micro_servers(self):
        """
        Initiates different micro servers.
        """
        self.album_photos_backend: AlbumPhotosBackend = AlbumPhotosBackend()

    def start(self, port: int = None):
        """
        Initiates the flask server.
        Inputs:
            - port: Desired port number.
        """
        self.flask_app.run(host="0.0.0.0", debug=self.debug, port=port)


if __name__ == "__main__":
    album_server_runner: AlbumServerRunner = AlbumServerRunner()
    album_server_runner.attach_micro_servers()
    album_server_runner.start(port=5050)