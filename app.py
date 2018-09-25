import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Instantiate the database
db = SQLAlchemy()


def create_app(script_info=None):
    # instantiate the app
    app = Flask(__name__)

    # set config
    app_settings = os.getenv('APP_SETTINGS')
    app.config.from_object(app_settings)

    db.init_app(app)

    app.shell_context_processor({'app': app, 'db': db})
    return app
