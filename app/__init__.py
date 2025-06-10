from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# SQLAlchemy database instance
db = SQLAlchemy()

# create and configure the app

def create_app():
    """Application factory."""
    app = Flask(__name__)

    # Default configuration uses local SQLite database
    if not app.config.get("SECRET_KEY"):
        app.config["SECRET_KEY"] = "dev-secret-key"
    app.config.setdefault("SQLALCHEMY_DATABASE_URI", "sqlite:///app.db")
    app.config.setdefault("SQLALCHEMY_TRACK_MODIFICATIONS", False)

    db.init_app(app)

    from .routes import bp as routes_bp
    app.register_blueprint(routes_bp)

    register_cli_commands(app)

    return app


def register_cli_commands(app):
    """Register custom CLI commands."""
    @app.cli.command("init-db")
    def init_db_command():
        """Initialize the database with default data."""
        from .models import Product

        db.drop_all()
        db.create_all()

        initial_products = [
            Product(name="Apples", quantity=20),
            Product(name="Oranges", quantity=15),
            Product(name="Potatoes", quantity=30),
        ]
        db.session.add_all(initial_products)
        db.session.commit()
        print("Initialized the database with sample data.")
