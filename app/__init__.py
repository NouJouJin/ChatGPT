from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# SQLAlchemy database instance
db = SQLAlchemy()
login_manager = LoginManager()

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
    login_manager.init_app(app)
    login_manager.login_view = 'routes.login'

    from .routes import bp as routes_bp
    app.register_blueprint(routes_bp)

    register_cli_commands(app)

    @login_manager.user_loader
    def load_user(user_id):
        from .models import User
        return User.query.get(int(user_id))

    return app


def register_cli_commands(app):
    """Register custom CLI commands."""
    @app.cli.command("init-db")
    def init_db_command():
        """Initialize the database with default data."""
        from .models import Product, User
        from werkzeug.security import generate_password_hash

        db.drop_all()
        db.create_all()

        initial_products = [
            Product(name="Apples", quantity=20),
            Product(name="Oranges", quantity=15),
            Product(name="Potatoes", quantity=30),
        ]
        db.session.add_all(initial_products)
        admin = User(username="admin", password_hash=generate_password_hash("password"), is_admin=True)
        db.session.add(admin)
        db.session.commit()
        print("Initialized the database with sample data.")
