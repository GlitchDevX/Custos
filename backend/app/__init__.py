from flask import Flask
from flask_restx import Api
from .resources.metrics import ns_metric
from .resources.mail_adress import ns_mail
from .utils.sqlalchemy_utils import SQLAlchemyWrapper
from .models.model_metrics import Metrics

db = SQLAlchemyWrapper().database

def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    api = Api(app, version='0.1.0-dev', title='Custos',
              description='A RESTful api for user content management')

    api.add_namespace(ns_metric)
    api.add_namespace(ns_mail)

    db.init_app(app)

    with app.app_context():
        db.create_all()

    return app