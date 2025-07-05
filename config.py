import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DB_FILE = os.path.join(BASE_DIR, "api", "database", os.getenv("DATABASE_FILE"))

class Config:
    CACHE_TYPE = "RedisCache"
    CACHE_REDIS_HOST = os.getenv("CACHE_REDIS_HOST")
    CACHE_REDIS_PORT = os.getenv("CACHE_REDIS_PORT")
    CACHE_REDIS_DB = os.getenv("CACHE_REDIS_DB")
    CACHE_DEFAULT_TIMEOUT = 300
    SQLALCHEMY_DATABASE_URI = f"sqlite+pysqlite:///{DB_FILE}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True