from typing import List
from sqlalchemy import delete, select, update
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from app.config import app_config
from app.models.flagged_content import FlaggedContent
from app.models.metric import Metric
from app.models.reported_content import ReportedContent


class DatabaseConnector:
    
    def __init__(self):
        db_uri = app_config.config.DB_URI
        self.engine = create_engine(db_uri)

    def get_all_reported_content(self):
        with Session(self.engine) as session:
            statement = select(ReportedContent)
            return session.scalars(statement).all()

    def write_results(self, flagged_data: List[FlaggedContent]):
        with Session(self.engine) as session:
            for row in flagged_data:
                session.add(row)
            session.commit()

    def remove_reports(self, report_ids):
        with Session(self.engine) as session:
            for r_id in report_ids:
                statement = delete(ReportedContent).where(ReportedContent.report_id == r_id)
                session.execute(statement)
            session.commit()

    def increase_metric(self, metric_name):
        with Session(self.engine) as session:
            statement = select(Metric).where(Metric.metric_name == metric_name)
            metric = session.scalar(statement)
            if metric:
                update_statement = update(Metric).where(Metric.metric_name == metric_name).values(data=metric.data + 1)
                session.execute(update_statement)
                session.commit()
