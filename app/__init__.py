from flask import Flask

# create and configure the app

def create_app():
    app = Flask(__name__)

    from .routes import bp as routes_bp
    app.register_blueprint(routes_bp)

    return app
