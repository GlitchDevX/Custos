from flask_sqlalchemy import SQLAlchemy
from .. import db

class Metrics(db.Model):
    __tablename__ = 'metrics'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    emailadress = db.Column(db.String(120), nullable=False)
    invalid_format = db.Column(db.Boolean, nullable=True)
    no_dns_record = db.Column(db.Boolean, nullable=True)
    spam_mail = db.Column(db.Boolean, nullable=True)
