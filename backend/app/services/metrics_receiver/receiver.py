from typing import List
from ...models.metric import Metric


def _filter_response(result) -> List[dict]:
    return [row.filter_state() for row in result]

class MetricsReceiver:

    @staticmethod
    def get_email_metrics():
        return {
            "metric": Metric.query.all()
        }
