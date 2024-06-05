from flask import Flask
from .routes import short
from .extensions import db


def create_app(config_file='settings.py'):
    
    app=Flask(__name__)

    app.config.from_pyfile(config_file)

    db.init_app(app)
    with app.app_context():
        db.create_all()

    app.register_blueprint(short)
    return app



