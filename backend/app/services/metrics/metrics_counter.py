from .metrics_helper import get_metrics_exporter
from typing import Literal

type all_metrics = Literal[
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

def count_metric(metric: all_metrics):
    exporter = get_metrics_exporter()
    namespace, label = metric.split('_', 1)
    
    exporter.counter(
        name="custos_" + namespace.lower(),
        description=f"Total Custos metrics for {namespace.lower()} namespace",
        labels=label
    )
