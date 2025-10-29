from app.utils.common_responses import ENDPOINT_DISABLED, ENDPOINT_DISABLED_MODEL
from flask import Response
from flask_restx import Resource, Namespace, fields

from app.services.metrics.metrics_reporter import MetricsReporter

ns_metric = Namespace('metrics', description='Metrics')

endpoint_disabled_model = ns_metric.model("endpoint_disabled", ENDPOINT_DISABLED_MODEL)

@ns_metric.route('') # no trailing slash to match prometheus metrics path style
class MetricsResource(Resource):
    """
    A resource class for reporting prometheus metrics.
    """
    metrics_reporter = MetricsReporter()

    @ns_metric.response(200, 'Prometheus Metrics', fields.String())
    @ns_metric.response(503, 'Endpoint Disabled', endpoint_disabled_model)
    def get(self):
        """
        Metrics

        Returns service usage metrics as well as some generic flask metrics in the prometheus format.
        """
        metrics = self.metrics_reporter.generate_metrics_report()
        if isinstance(metrics, tuple):
            return metrics
        
        return Response(metrics, mimetype='text/plain')