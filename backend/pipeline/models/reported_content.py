from sqlalchemy import Column, DateTime, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
class ReportedContent(Base):
    __tablename__ = 'reported_content'
    
    report_id = Column(String(50), primary_key=True)
    reported_at = Column(DateTime())
    user_id = Column(String(100))
    content = Column(String(5000))
