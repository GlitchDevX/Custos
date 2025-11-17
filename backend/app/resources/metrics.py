from flask import Response
from flask_restx import Resource, Namespace, fields

from app.services.metrics.metrics_reporter import MetricsReporter
from app.utils.common_responses import ENDPOINT_DISABLED_MODEL

ns_metric = Namespace('Metrics', description='Endpoint for getting metrics for Prometheus.', path='/metrics')

endpoint_disabled_model = ns_metric.model("endpoint_disabled", ENDPOINT_DISABLED_MODEL)

@ns_metric.route('/', strict_slashes=False)
class MetricsResource(Resource):
    """
    A resource class for reporting prometheus metrics.
    """
    metrics_reporter = MetricsReporter()

    @ns_metric.response(200, 'Prometheus Metrics', fields.String())
    @ns_metric.response(503, 'Endpoint Disabled', endpoint_disabled_model)
    def get(self):
        """
        /metrics

        Returns service usage metrics as well as some generic Flask metrics in the Prometheus format.
        """
        metrics = self.metrics_reporter.generate_metrics_report()
        if isinstance(metrics, tuple):
            return metrics
        
        return Response(metrics, mimetype='text/plain')