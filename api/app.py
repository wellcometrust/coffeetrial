import os
from flask_cors import CORS
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Instantiate the database
db = SQLAlchemy()


def create_app(script_info=None):
    # instantiate the app
    app = Flask(__name__,  static_folder='static')

    # enable CORS
    CORS(app)
    # set config
    app_settings = os.getenv('APP_SETTINGS')
    app.config.from_object(app_settings)

    db.init_app(app)
    from admin.user import user_blueprint
    from admin.round import round_blueprint
    from admin.matches import matches_blueprint
    app.register_blueprint(user_blueprint)
    app.register_blueprint(round_blueprint)
    app.register_blueprint(matches_blueprint)

    from client.matching import matching_blueprint
    from client.authentication import auth_blueprint
    app.register_blueprint(matching_blueprint)
    app.register_blueprint(auth_blueprint)

    app.shell_context_processor({'app': app, 'db': db})
    return app
