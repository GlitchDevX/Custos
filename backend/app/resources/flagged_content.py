from flask_restx import Resource, Namespace
from flask import request

ns_report = Namespace('flagged-content', description='Endpoint to get results from pipeline')
parser = ns_report.parser()
parser.add_argument('reportId', type=str, required=True)

@ns_report.route('/')
class FlaggedContentResource(Resource):

    @ns_report.expect(parser)
    def get(self):
        parser.parse_args(strict=True)
        reportId = request.json["reportId"]
        
