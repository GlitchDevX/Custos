from datetime import datetime
from typing import List
from sqlalchemy import create_engine, delete, select
from app.config import Config, DevelopmentConfig
from sqlalchemy.orm import Session

from .models.reported_content import ReportedContent
from .models.flagged_content import FlaggedContent

class DatabaseConnector:
    
    def __init__(self):
        db_uri = DevelopmentConfig.SQLALCHEMY_DATABASE_URI
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
            for id in report_ids:
                statement = delete(ReportedContent).where(ReportedContent.report_id == id)
                session.execute(statement)
            session.commit()
