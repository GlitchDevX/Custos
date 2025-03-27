from app import create_app
from app.config import TestingConfig
import pytest

@pytest.fixture()
def app():
    app = create_app(TestingConfig)
    yield app

@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()