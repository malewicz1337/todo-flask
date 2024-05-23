import pytest
from app.app import create_app
from app.extensions import db as _db
from sqlalchemy.orm import scoped_session, sessionmaker


@pytest.fixture(scope="session")
def app():
    app = create_app()
    app.config.update(
        {
            "TESTING": True,
            "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:",
        }
    )
    with app.app_context():
        yield app


@pytest.fixture(scope="session")
def db(app):
    _db.app = app
    _db.create_all()
    yield _db
    _db.drop_all()


@pytest.fixture(scope="function")
def session(db):
    connection = db.engine.connect()
    transaction = connection.begin()

    options = dict(bind=connection, binds={})
    session_factory = sessionmaker(**options)
    Session = scoped_session(session_factory)

    db.session = Session
    yield db.session

    transaction.rollback()
    connection.close()
    Session.remove()


@pytest.fixture(scope="function")
def client(app):
    return app.test_client()
