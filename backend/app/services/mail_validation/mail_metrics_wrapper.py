from backend.app.models.metric import Metric
from .validation_result import ValidationResult

from ...utils.sqlalchemy_utils import SQLAlchemyWrapper

class MailMetricsWrapper:

    def __init__(self):
        self.db = SQLAlchemyWrapper().database

    def save_mail_metric(self, result: ValidationResult):
        metric = Metric.query.get(result.code)
        metric.data += 1
        self.db.session.commit()
    