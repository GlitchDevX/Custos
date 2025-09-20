from flask import Response
from flask_restx import Resource, Namespace

from app.services.metrics.metrics_reporter import MetricsReporter

ns_metric = Namespace('metrics', description='Metrics')

@ns_metric.route('') # no trailing slash to match prometheus metrics path style
class MetricsResource(Resource):
    """
    A resource class for reporting prometheus metrics.
    """
    metrics_reporter = MetricsReporter()

    def get(self):
        metrics = self.metrics_reporter.generate_metrics_report()
        if isinstance(metrics, tuple):
            return metrics
        
        return Response(metrics, mimetype='text/plain')