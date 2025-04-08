from datetime import date, datetime
from flask_restx import Resource, Namespace

from app.services.deep_check.result_consumer import ResultConsumer

ns_flagged = Namespace('flagged-content', description='Endpoint to get results from pipeline')
parser = ns_flagged.parser()
parser.add_argument('reportId', type=str)
parser.add_argument('reportedAt', type=lambda s: datetime.strptime(s, "%Y-%m-%d").date())
parser.add_argument('processedAt', type=lambda s: datetime.strptime(s, "%Y-%m-%d").date())
parser.add_argument('remove', type=bool, default=False)

@ns_flagged.route('/')
class FlaggedContentResource(Resource):
    result_consumer=ResultConsumer()

    @ns_flagged.expect(parser)
    def get(self):
        args = parser.parse_args(strict=True)
        report_id = args["reportId"]
        reported_at = args["reportedAt"]
        processed_at = args["processedAt"]
        remove = args["remove"]
        
        return self.result_consumer.consume_results(report_id, reported_at, processed_at, remove)
        
