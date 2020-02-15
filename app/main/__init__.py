import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from flask_redis import FlaskRedis
from flask_uploads import configure_uploads, patch_request_class
from app.main.libs.image_helper import IMAGE_SET
from pyfcm import FCMNotification
from .config import config_by_name

db = SQLAlchemy()
flask_bcrypt = Bcrypt()
redis_client = FlaskRedis()
def create_app(config_name):
    app = Flask(__name__)
    CORS(app)
    app.config.from_object(config_by_name[config_name])
    patch_request_class(app, 10 * 1024 * 1024)  # restrict max upload image size to 10MB
    configure_uploads(app, IMAGE_SET)
    db.init_app(app)
    flask_bcrypt.init_app(app)
    redis_client.init_app(app)

    return app