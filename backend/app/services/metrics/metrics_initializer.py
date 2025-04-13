from typing import Dict

from sqlalchemy.orm import Session
from sqlalchemy import select, update, delete
from app.models.metric import Metric

ALL_METRICS = [
    "MAIL_OK",
    "MAIL_FORMAT_INVALID",
    "MAIL_DISPOSABLE",
    "MAIL_NO_SERVER",
    "MAIL_INVALID_DOMAIN",
    "MAIL_SMTP_DISCONNECT",
    "MAIL_SMTP_CONNECTION_ERROR",
    "MAIL_SMTP_TIMEOUT",

    "REALTIME_EXECUTED_CHECK",
    "REALTIME_URL_DETECTED",
    "REALTIME_BLOCKED_WORD_DETECTED",

    "PIPELINE_EXECUTED_CHECK",
    "PIPELINE_FALSE_REPORT",
]
class MetricsManager:

    def __init__(self, db):
        self.db = db

    def create_all(self):
        session: Session
        with self.db.session() as session:
            all_db_metrics: Dict[str, int] = {}
            for row in session.execute(select(Metric.metric_name, Metric.index)):
                all_db_metrics[row[0]] = row[1]

            print(all_db_metrics)

            for index, metric in enumerate(ALL_METRICS):
                if metric not in all_db_metrics.keys():
                    metric_entry = Metric(metric_name=metric, index=index, data=0)
                    session.add(metric_entry)
                elif index != all_db_metrics[metric]:
                    statement = update(Metric).where(Metric.metric_name == metric).values(index=index)
                    session.execute(statement)

            for removed_metric in filter(lambda m: m not in ALL_METRICS, all_db_metrics):
                session.execute(delete(Metric).where(Metric.metric_name == removed_metric))

            session.commit()
