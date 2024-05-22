from flask import Flask

from .extensions import db, ma
from .tasks.routes import task_bp

app = Flask(__name__)
app.register_blueprint(task_bp)

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://user:password@localhost/todo_db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


db.init_app(app)
ma.init_app(app)


@app.route("/")
def home():
    return "Hello, World!"


if __name__ == "__main__":
    app.run(debug=True)
