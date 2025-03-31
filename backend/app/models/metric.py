from ..utils.sqlalchemy_utils import SQLAlchemySingleton

db = SQLAlchemySingleton()

class Metric(db.Model):
    __tablename__ = 'metrics'
    
    metric_name = db.Column(db.String(50), primary_key=True)
    data = db.Column(db.Integer)

    def filter_state(self):
        del self.__dict__['_sa_instance_state']
        return self.__dict__
    
    @staticmethod
    def increase(metric_name):
        metric = Metric.query.filter_by(metric_name=metric_name).first()
        if metric:
            metric.data += 1
            db.session.commit()
