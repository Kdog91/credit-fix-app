from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

# Initialize extensions
db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
def create_app():
    app = Flask(__name__)

    # Configurations for secret key and database
    app.config['SECRET_KEY'] = 'your_secret_key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///instance/credit_fix_app.db'

    # Initialize extensions
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    # Set login view for login-required routes
    login_manager.login_view = 'routes.login'

    # Import and register the blueprint
    from app.routes import routes
    app.register_blueprint(routes)

    return app
