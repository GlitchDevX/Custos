from prometheus_flask_exporter import RESTfulPrometheusMetrics
from flask.globals import current_app

def get_metrics_exporter() -> RESTfulPrometheusMetrics:
    return current_app.metrics_exporter # type: ignore