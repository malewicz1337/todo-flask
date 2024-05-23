from app.extensions import db, ma
from app.tasks.routes import task_bp
from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = (
        "mysql+pymysql://user:password@localhost/todo_db"
    )
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    ma.init_app(app)

    app.register_blueprint(task_bp)

    return app
