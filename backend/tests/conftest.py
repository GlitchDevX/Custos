from app.config.flask_config import FlaskTstConfig
from app.app import FlaskApplication
import pytest

@pytest.fixture()
def app():
    app = FlaskApplication(FlaskTstConfig)
    yield app.flask_app

@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()