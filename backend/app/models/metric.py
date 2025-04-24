import logging

from ..utils.sqlalchemy_utils import SQLAlchemySingleton
from sqlalchemy import Column, String, Integer

db = SQLAlchemySingleton()

class Metric(db.Model):
    __tablename__ = 'metrics'
    
    metric_name = Column(String(50), primary_key=True)
    index = Column(Integer)
    data = Column(Integer)

    def filter_state(self):
        del self.__dict__['_sa_instance_state']
        return self.__dict__
    
    @staticmethod
    def increase(metric_name):
        with db.session() as session:
            metric = Metric.query.filter_by(metric_name=metric_name).first()
            if metric:
                metric.data += 1
                session.commit()
            else:
                logging.warning(f"Tried to increase metric with name '{metric_name}', but it does not exist.")
