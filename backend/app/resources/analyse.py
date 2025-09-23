from flask import request
from flask_restx import Resource, Namespace

from ..services.analyse.analyser import AnalyserService

ns_analyse = Namespace('analyze', description='Endpoint for deep content analysis')
parser = ns_analyse.parser()
parser.add_argument('content', type=str, required=True, location='json')

@ns_analyse.route('/')
class AnalyseResource(Resource):
    """
    A resource class for analysing content with the detoxify model.
    """
    analyser_service = AnalyserService()

    @ns_analyse.expect(parser)
    def post(self):
        args = parser.parse_args(strict=True)
        content = args["content"]
        result = self.analyser_service.analyse_content(content)
        return result
    