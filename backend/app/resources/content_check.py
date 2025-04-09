from ..services.content_check.content_checker import ContentCheckService
from flask_restx import Resource, Namespace, fields, Model, Api
from flask import request

ns_content_check = Namespace('content', description='Endpoint for Content Check')
parser = ns_content_check.parser()
parser.add_argument('content', type=str, required=True, location='json')

@ns_content_check.route('/')
class ContentCheckResource(Resource):
    """
    A resource class for checking content against certain criteria.
    """
    content_service = ContentCheckService()

    @ns_content_check.expect(parser)
    def post(self):
        parser.parse_args(strict=True)
        content = request.json["content"]
        result = self.content_service.check_content(content)
        return result
    