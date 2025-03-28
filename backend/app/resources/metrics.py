from flask_restx import Resource, Namespace
from ..services.metrics_receiver.receiver import MetricsReceiver
from flask import jsonify

ns_metric = Namespace('metrics', description='Metrics')

@ns_metric.route('/')
class MetricsResource(Resource):

    def get(self):
        metrics = MetricsReceiver.get_email_metrics()
        return jsonify(metrics)