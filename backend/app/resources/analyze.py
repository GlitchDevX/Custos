from flask import request
from flask_restx import Resource, Namespace

from ..services.analyze.analyzer import AnalyzerService

ns_analyze = Namespace('analyze', description='Endpoint for deep content analysis')
parser = ns_analyze.parser()
parser.add_argument('content', type=str, required=True, location='json')

@ns_analyze.route('/')
class analyzeResource(Resource):
    """
    A resource class for analysing content with the detoxify model.
    """
    analyzer_service = AnalyzerService()

    @ns_analyze.expect(parser)
    def post(self):
        args = parser.parse_args(strict=True)
        content = args["content"]
        result = self.analyzer_service.analyze_content(content)
        return result
    