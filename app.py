from flask import Flask
from extensions import db
from route import bug_routes
from models import Bug

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'supersecretkey'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bugtracker.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    with app.app_context():
        db.create_all()

    app.register_blueprint(bug_routes)
    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
