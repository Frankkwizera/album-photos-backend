__author__ = "Frank Kwizera"

from src import __APP_NAME__
from flask import Flask

__the_app__: Flask = None

def __create_app(testing: bool = False):
    flask_app: Flask = Flask(__APP_NAME__, template_folder=None, static_folder=None)
    flask_app.secret_key = "TEST SECRET KEY"
    return flask_app

__the_app__: Flask = None

def get_flask_app(testing: bool = False):
    global __the_app__
    if __the_app__ is None:
        __the_app__ = __create_app(testing=testing)
    return __the_app__