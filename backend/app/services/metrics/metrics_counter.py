from app.utils.singleton_meta import SingletonMeta
from typing import Literal
from prometheus_client import Counter

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
        self._init_metrics()

    def _init_metrics(self):
        self.counter = Counter("custos_service_metrics", "Total Custos service metrics", ['namespace',  'label'])

    def count_metric(self, metric: Metric):
        namespace, label = metric.split('_', 1)
        self.counter.labels(namespace=namespace, label=label).inc()

def count_metric(metric: Metric):
    MetricsCounter().count_metric(metric)