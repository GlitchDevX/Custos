from flask_restx import Resource, Namespace

ns_metric = Namespace('metrics', description='Metrics')

@ns_metric.route('/')
class MetricsResource(Resource):

    def get(self):
        return 200