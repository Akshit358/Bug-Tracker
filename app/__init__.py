from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your-secret-key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bugs.db'
    
    db.init_app(app)

    from ..models import BugReport
    from .routes import main
    app.register_blueprint(main)

    return app
