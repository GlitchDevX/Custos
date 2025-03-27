from flask import Flask
from flask_restx import Api
from .resources.metrics import ns_metric
from .resources.mail_adress import ns_mail

def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    api = Api(app, version='0.1.0-dev', title='Custos',
              description='A RESTful api for user content management')

    api.add_namespace(ns_metric)
    api.add_namespace(ns_mail)

    return app