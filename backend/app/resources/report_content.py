from flask_restx import Resource, Namespace
from flask import request

from app.services.deep_check.pipeline_submitter import PipelineSubmitter

ns_report = Namespace('report-content', description='Endpoint for reporting content to submit into pipeline')
parser = ns_report.parser()
parser.add_argument('userId', type=str, required=True, location='json')
parser.add_argument('content', type=str, required=True, location='json')

@ns_report.route('/')
class MailValidationResource(Resource):
    pipeline_submitter = PipelineSubmitter()

    @ns_report.expect(parser)
    def post(self):
        parser.parse_args(strict=True)
        userId = request.json["userId"]
        content = request.json["content"]
        return self.pipeline_submitter.submit(userId, content)