from flask import Flask
from app.views import tasks


def use(app: Flask) -> None:
    app.register_blueprint(tasks)