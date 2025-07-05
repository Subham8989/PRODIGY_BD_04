from flask_restful import Api
from flask_caching import Cache
from flask_sqlalchemy import SQLAlchemy

api = Api()
cache = Cache()
db = SQLAlchemy()