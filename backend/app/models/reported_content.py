from datetime import datetime
from ..utils.sqlalchemy_utils import SQLAlchemySingleton

db = SQLAlchemySingleton()

class ReportedContent(db.Model):
    __tablename__ = 'reported_content'
    
    report_id = db.Column(db.String(50), primary_key=True)
    reported_at = db.Column(db.DateTime, default=datetime.now())
    user_id = db.Column(db.String(100))
    content = db.Column(db.String(5000))
