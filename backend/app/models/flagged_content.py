from datetime import datetime
from ..utils.sqlalchemy_utils import SQLAlchemySingleton
from sqlalchemy import Column, String, DateTime, Boolean

db = SQLAlchemySingleton()

class FlaggedContent(db.Model):
    __tablename__ = 'flagged_content'
    
    report_id = Column(String(50), primary_key=True)
    reported_at = Column(DateTime())
    processed_at = Column(DateTime, default=datetime.now())
    user_id = Column(String(100))
    content = Column(String(5000))
    false_report = Column(Boolean())
    flags = Column(String(200)) # comma separated list
