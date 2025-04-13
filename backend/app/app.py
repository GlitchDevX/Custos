from flask import Flask
from flask_cors import CORS
from flask_restx import Api

from app.services.metrics.metrics_initializer import MetricsManager
from .resources.metrics import ns_metric
from .resources.mail_adress import ns_mail
from .resources.config import ns_config
from .resources.content_check import ns_content_check
from .resources.report_content import ns_report
from .resources.flagged_content import ns_flagged
from .resources.pipeline import ns_pipeline
from .utils.sqlalchemy_utils import SQLAlchemySingleton

# Imports to generate tables

class FlaskApplication:
    """
    A class to initialize and configure a Flask application with RESTful API capabilities.

    Attributes:
        db (SQLAlchemySingleton): Singleton instance for database management.
        METRICS (list): A list of predefined metrics for monitoring mail and content checks.
        flask_app (Flask): The Flask application instance.
        
    :param config (Config): Configuration object containing application settings such as HOST, PORT, and DEBUG.
    """

    def __init__(self, config):
        self.db = SQLAlchemySingleton()
        self.metrics = MetricsManager(self.db)
        self.flask_app = Flask(__name__)
        self.flask_app.config.from_object(config)
        CORS(self.flask_app, origins="*")
        api = Api(self.flask_app, version='0.1.0-dev', title='Custos',
                  description='A RESTful api for user content management')

        api.add_namespace(ns_metric)
        api.add_namespace(ns_mail)
        api.add_namespace(ns_config)
        api.add_namespace(ns_content_check)
        api.add_namespace(ns_report)
        api.add_namespace(ns_flagged)
        api.add_namespace(ns_pipeline)

        self.db.init_app(self.flask_app)

        with self.flask_app.app_context():
            self.db.create_all()
            self.metrics.create_all()

        if not self.flask_app.config["TESTING"]:
            self.flask_app.run(host=config.HOST, port=config.PORT, debug=config.DEBUG)