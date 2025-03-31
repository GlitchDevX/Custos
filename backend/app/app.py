from flask import Flask
from flask_restx import Api
from .resources.metrics import ns_metric
from .resources.mail_adress import ns_mail
from .resources.config import ns_config
from .utils.sqlalchemy_utils import SQLAlchemySingleton
from .models.metric import Metric


class FlaskApplication:
    db = SQLAlchemySingleton()
    METRICS = ["MAIL_OK",
               "MAIL_FORMAT_INVALID",
               "MAIL_DISPOSABLE",
               "MAIL_NO_SERVER",
               "MAIL_INVALID_DOMAIN",
               "MAIL_SMTP_DISCONNECT",
               "MAIL_SMTP_CONNECTION_ERROR",
               "MAIL_SMTP_TIMEOUT"
               ]

    def __init__(self, config):
        app = Flask(__name__)
        app.config.from_object(config)
        api = Api(app, version='0.1.0-dev', title='Custos',
                  description='A RESTful api for user content management')

        api.add_namespace(ns_metric)
        api.add_namespace(ns_mail)
        api.add_namespace(ns_config)

        self.db.init_app(app)

        with app.app_context():
            self.db.create_all()

            for metric in self.METRICS:
                metric_row = Metric.query.filter_by(metric_name=metric).first()
                if not metric_row:
                    metric_entry = Metric(metric_name=metric, data=0)
                    self.db.session.add(metric_entry)

            self.db.session.commit()

        app.run(host=config.HOST, port=config.PORT, debug=config.DEBUG)