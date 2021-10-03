from flask import Flask


def create_app(config_name):
    app = Flask(__name__)
    app.config["JWT_SECRET_KEY"] = "secret-jwt"
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = False
    app.config['PROPAGATE_EXCEPTIONS'] = True
    return app