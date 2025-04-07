import uuid

from app.models.reported_content import ReportedContent

from ...utils.sqlalchemy_utils import SQLAlchemySingleton


db = SQLAlchemySingleton()

class PipelineSubmitter:
    
    def submit(self, userId, content):
        report = ReportedContent()
        report.report_id = uuid.uuid4()
        report.user_id = userId
        report.content = content

        db.session.add(report)
        db.session.commit()

        return {"code": "OK"}, 200