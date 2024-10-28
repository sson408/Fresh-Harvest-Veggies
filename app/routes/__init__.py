from flask import Blueprint, Flask

main = Blueprint('main', __name__)


def create_app():
    app = Flask(__name__)

    return app
