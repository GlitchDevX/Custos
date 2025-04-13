from typing import List
from ...models.metric import Metric


def _filter_response(result) -> List[dict]:
    return [row.filter_state() for row in result]

class MetricsReceiver:
    """
    Filters the response from the database query to return only the relevant metric information.
    """

    @staticmethod
    def get_all_metrics():
        return {
            "metrics": _filter_response(Metric.query.order_by(Metric.index).all())
        }
