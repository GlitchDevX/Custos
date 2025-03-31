from typing import List
from ...models.email_metrics import EmailMetrics


def _filter_response(result) -> List[dict]:
    return [row.filter_state() for row in result]

class MetricsReceiver:

    @staticmethod
    def get_email_metrics():
        result = {
            "total": EmailMetrics.query.count(),
            "invalid_format": EmailMetrics.query.filter(EmailMetrics.invalid_format == True).count(),
            "no_dns_record": EmailMetrics.query.filter(EmailMetrics.no_mailserver == True).count(),
            "spam_mail": EmailMetrics.query.filter(EmailMetrics.disposable == True).count()
        }
        return result
