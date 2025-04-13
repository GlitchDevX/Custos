from flask_restx import Resource, Namespace
from ..services.metrics.receiver import MetricsReceiver
from flask import jsonify

ns_metric = Namespace('metrics', description='Metrics')

@ns_metric.route('/')
class MetricsResource(Resource):
    """
    A resource class for managing metrics.
    """

    def get(self):
        metrics = MetricsReceiver.get_all_metrics()
        return jsonify(metrics)