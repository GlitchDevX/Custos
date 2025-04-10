import uuid

from app.models.reported_content import ReportedContent

from app.config_reader import ConfigReader
from app.utils.common_responses import ENDPOINT_DISABLED
from app.utils.sqlalchemy_utils import SQLAlchemySingleton


db = SQLAlchemySingleton()

class ContentReporter:

    def __init__(self):
        self.config = ConfigReader("pipeline")

    def submit(self, user_id, content):
        if not self.config.get("enabled"):
            return ENDPOINT_DISABLED

        report = ReportedContent()
        report.report_id = uuid.uuid4()
        report.user_id = user_id
        report.content = content

        db.session.add(report)
        db.session.commit()

        return {"code": "OK", "reportId": report.report_id}, 200