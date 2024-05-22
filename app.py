from flask import Flask
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

from config import Config
from routes import task_bp

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
ma = Marshmallow(app)


app.register_blueprint(task_bp, url_prefix="/tasks")

db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
