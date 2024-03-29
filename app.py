import config

from flask import Flask
from sqlalchemy import create_engine
from flask_cors import CORS

from model import WestaDao
from service import WestaService
from view import create_endpoints


class Services:
    pass


def create_app(test_config = None):
    app = Flask(__name__)

    CORS(app)

    if test_config is None:
        app.config.from_pyfile("config.py")
    else:
        app.config.update(test_config)

    database = create_engine(app.config["DB_URL"], encoding="utf-8", max_overflow=0)
    app.database = database
    
    ## Persistence Layer
    westa_dao = WestaDao(database)

    ## Business Layer

    services = Services
    services.westa_service = WestaService(westa_dao)

    create_endpoints(app, services)

    return app 
