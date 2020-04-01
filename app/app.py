from flask import Flask
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from flask_vuejs import Vue

db = SQLAlchemy()
ma = Marshmallow()
vue = Vue()

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///tasks.sqlite"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # register flask extensions
    db.init_app(app)
    ma.init_app(app)
    vue.init_app(app)

    from . import routes
    routes.use(app)

    return app
