from flask import Flask, request
from flask_cors import CORS
from flask_restx import Api
from prometheus_flask_exporter import RESTfulPrometheusMetrics

from .resources.analyse import ns_analyse
from .resources.metrics import ns_metric
from .resources.mail_adress import ns_mail
from .resources.config import ns_config
from .resources.content_check import ns_content_check

class FlaskApplication:
    """
    A class to initialize and configure a Flask application with RESTful API capabilities.

    Attributes:
        flask_app (Flask): The Flask application instance.
        
    :param config (Config): Configuration object containing application settings such as HOST, PORT, and DEBUG.
    """

    def __init__(self, config):
        self.flask_app = Flask(__name__)
        self.flask_app.config.from_object(config)
        CORS(self.flask_app, origins="*")
        api = Api(self.flask_app, version='1.0.0', title='Custos',
                  description='Modular user-content management system written in Python.')
        if not self.flask_app.config["TESTING"]:
            self.metrics = RESTfulPrometheusMetrics(app=None, api=api)

        api.add_namespace(ns_metric)
        api.add_namespace(ns_mail)
        api.add_namespace(ns_config)
        api.add_namespace(ns_content_check)
        api.add_namespace(ns_analyse)


        if not self.flask_app.config["TESTING"]:
            with self.flask_app.app_context():
                self.metrics.init_app(self.flask_app)
                self.metrics.register_default(
                    self.metrics.counter('flask_http_request_by_path_counter', 'Requests count by request paths',
                         labels={'path': lambda: request.path, 'method': lambda: request.method }
                    )
                )
                self.flask_app.metrics_exporter = self.metrics # type: ignore


        if not self.flask_app.config["TESTING"]:
            self.flask_app.run(host=config.HOST, port=config.PORT, debug=config.DEBUG)