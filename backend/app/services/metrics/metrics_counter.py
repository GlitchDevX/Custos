from typing import Callable
from typing import Any
from typing import Dict
from app.utils.singleton_meta import SingletonMeta
from .metrics_helper import get_metrics_exporter
from typing import Literal

type Metric = Literal[
    "MAIL_OK",
    "MAIL_FORMAT_INVALID",
    "MAIL_DISPOSABLE",
    "MAIL_NO_SERVER",
    "MAIL_NO_ADDRESS",
    "MAIL_INVALID_DOMAIN",
    "MAIL_SMTP_DISCONNECT",
    "MAIL_SMTP_CONNECTION_ERROR",
    "MAIL_SMTP_TIMEOUT",

    "REALTIME_EXECUTED_CHECK",
    "REALTIME_URL_DETECTED",
    "REALTIME_BLOCKED_WORD_DETECTED",

    "ANALYZER_EXECUTED",
    "ANALYZER_TOXICITY_DETECTED"
]
all_metrics: list[Metric] = [
    "MAIL_OK",
    "MAIL_FORMAT_INVALID",
    "MAIL_DISPOSABLE",
    "MAIL_NO_SERVER",
    "MAIL_NO_ADDRESS",
    "MAIL_INVALID_DOMAIN",
    "MAIL_SMTP_DISCONNECT",
    "MAIL_SMTP_CONNECTION_ERROR",
    "MAIL_SMTP_TIMEOUT",

    "REALTIME_EXECUTED_CHECK",
    "REALTIME_URL_DETECTED",
    "REALTIME_BLOCKED_WORD_DETECTED",

    "ANALYZER_EXECUTED",
    "ANALYZER_TOXICITY_DETECTED"
]

class MetricsCounter(metaclass=SingletonMeta):
    def __init__(self):
        print("Creating metrics")
        self._init_metrics()

    def _init_metrics(self):
        self.counters: Dict[Metric, Callable] = dict()
        for metric in all_metrics:
            self.create_metric(metric)
            print(f"Created metric: {metric}")

    def create_metric(self, metric: Metric):
        exporter = get_metrics_exporter()
        # add check if exporter not present and then log the metric and not count it because in dev mode
        namespace, label = metric.split('_', 1)
        metric_counter = exporter.counter(
            name="custos_service_metrics",
            description=f"Total Custos service metrics",
            labels={'namespace': namespace, 'label': label}
        )
        self.counters[metric] = metric_counter
        

    def count_metric(self, metric: Metric):
        self.counters[metric]()

def count_metric(metric: Metric):
    MetricsCounter().count_metric(metric)