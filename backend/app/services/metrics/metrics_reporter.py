from app.services.metrics.metrics_helper import get_metrics_exporter
from flask import current_app
from app.config_reader import ConfigReader
from app.utils.common_responses import ENDPOINT_DISABLED


class MetricsReporter:
    """
    A class to report metrics tracked by the prometheus metrics exporter.
    """

    def __init__(self) -> None:
        self.config = ConfigReader("metrics")

    def generate_metrics_report(self) -> tuple | str:
        if not self.config.get("enabled"):
            return ENDPOINT_DISABLED

        metrics = get_metrics_exporter().generate_metrics()[0]
        return metrics