from ..services.analyse.analyser import AnalyserService
from ..services.content_check.content_checker import ContentCheckService
from flask_restx import Resource, Namespace, fields, Model, Api
from flask import request

ns_analyse = Namespace('analyse', description='Endpoint for deep content analysis')
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
        parser.parse_args(strict=True)
        content = request.json["content"]
        result = self.analyser_service.analyse_content(content)
        return result
    