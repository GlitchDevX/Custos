from datetime import datetime
from ..utils.sqlalchemy_utils import SQLAlchemySingleton
from sqlalchemy import Column, String, DateTime

db = SQLAlchemySingleton()

class ReportedContent(db.Model):
    __tablename__ = 'reported_content'
    
    report_id = Column(String(50), primary_key=True)
    reported_at = Column(DateTime, default=datetime.now())
    user_id = Column(String(100))
    content = Column(String(5000))
