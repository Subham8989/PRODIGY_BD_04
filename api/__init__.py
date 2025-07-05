from flask import Flask

from ..extensions import api, cache, db
from ..config import Config
from .routes import UsersRoute

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    api.add_resource(UsersRoute, "/users")
    api.init_app(app)
    cache.init_app(app)
    db.init_app(app)
    with app.app_context():
        db.create_all()
    return app