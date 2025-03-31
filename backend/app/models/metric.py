from ..utils.sqlalchemy_utils import SQLAlchemyWrapper
from .base_model import BaseModel

db = SQLAlchemyWrapper().database

class Metric(db.Model):
    __tablename__ = 'metrics'
    
    metric_name = db.Column(db.String(50), primary_key=True)
    data = db.Column(db.Integer)

    def filter_state(self):
        del self.__dict__['_sa_instance_state']
        return self.__dict__
