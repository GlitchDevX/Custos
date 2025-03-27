from flask import Flask
from flask_restx import Api
from .resources.metrics import ns_metric
from .resources.mail_adress import ns_mail
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    api = Api(app, version='0.1.0-dev', title='Custos',
              description='A RESTful api for user content management')

    api.add_namespace(ns_metric)
    api.add_namespace(ns_mail)

    db.init_app(app)

    with app.app_context():
        from .models.metrics import Metrics
        db.create_all()

    return app