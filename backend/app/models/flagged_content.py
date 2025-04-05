from ..utils.sqlalchemy_utils import SQLAlchemySingleton

db = SQLAlchemySingleton()

class ReportedContent(db.Model):
    __tablename__ = 'flagged_content'
    
    report_id = db.Column(db.String(50), primary_key=True)
    user_id = db.Column(db.String(100))
    content = db.Column(db.String(5000))
    flags = db.Column(db.String(200)) # comma separated list
