import pytest
from config import TestConfig
from app import create_app, db


@pytest.fixture
def application():
    test_app = create_app(TestConfig)
    yield test_app


@pytest.fixture
def database(application):
    with application.app_context():
        db.create_all()
        yield db
        db.drop_all()
