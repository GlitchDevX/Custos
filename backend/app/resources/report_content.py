from flask_restx import Resource, Namespace
from flask import request

from app.services.deep_check.content_reporter import ContentReporter

ns_report = Namespace('report-content', description='Endpoint for reporting content to submit into pipeline')
parser = ns_report.parser()
parser.add_argument('userId', type=str, required=True, location='json')
parser.add_argument('content', type=str, required=True, location='json')

@ns_report.route('/')
class ReportContentResource(Resource):
    content_reporter = ContentReporter()

    @ns_report.expect(parser)
    def post(self):
        parser.parse_args(strict=True)
        userId = request.json["userId"]
        content = request.json["content"]
        return self.content_reporter.submit(userId, content)