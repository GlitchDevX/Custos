from app.config import TestingConfig
from app.app import FlaskApplication
import pytest

@pytest.fixture()
def app():
    app = FlaskApplication(TestingConfig)
    yield app.flask_app

@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()