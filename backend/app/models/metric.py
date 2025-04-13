from ..utils.sqlalchemy_utils import SQLAlchemySingleton
from sqlalchemy import Column, String, Integer

db = SQLAlchemySingleton()

class Metric(db.Model):
    __tablename__ = 'metrics'
    
    metric_name = Column(String(50), primary_key=True)
    data = Column(Integer)

    def filter_state(self):
        del self.__dict__['_sa_instance_state']
        return self.__dict__
    
    @staticmethod
    def increase(metric_name):
        metric = Metric.query.filter_by(metric_name=metric_name).first()
        if metric:
            metric.data += 1
            db.session.commit()
