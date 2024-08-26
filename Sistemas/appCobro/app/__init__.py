from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()

def create_app(test_config=None):
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__, instance_relative_config=True)


    #Basic test route
    @app.route("/hello")
    def hello():
        return 'HEllo'
    

    """Initialize"""
    login_manager.init_app(app)
    bcrypt.init_app(app)
    db.init_app(app)
    migrate = Migrate(app, db)

    """Blueprints"""
    from routes import admin as admin_blueprint
    app.register_blueprint(admin_blueprint)
    

    """Obtener usuario actual para cada solicitud"""
    from app.models import Usuario
    login_manager.login_view = "admin.login"
    login_manager.login_message_category = "danger"
    @login_manager.user_loader
    def load_user(user_id):
        return Usuario.query.get(int(user_id)) #.filter(Usuario.id == int(user_id)).first()
    
    return app