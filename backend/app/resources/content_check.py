from ..services.content_check.content_checker import ContentCheckService
from flask_restx import Resource, Namespace, fields, Model, Api
from flask import request

from ..utils.common_responses import ENDPOINT_DISABLED_MODEL

ns_content_check = Namespace('Content', description='Endpoint checking content against certain criteria.', path='/content')
parser = ns_content_check.parser()
parser.add_argument('content', type=str, required=True, location='json')

content_result_model = ns_content_check.model("content_result", {
    'flags': fields.List(fields.String()),
    'censored_content': fields.String()
})
endpoint_disabled_model = ns_content_check.model("endpoint_disabled", ENDPOINT_DISABLED_MODEL)

@ns_content_check.route('/', strict_slashes=False)
class ContentCheckResource(Resource):
    """
    A resource class for checking content against certain criteria.
    """
    content_service = ContentCheckService()

    @ns_content_check.response(503, "Endpoint Disabled", endpoint_disabled_model)
    @ns_content_check.response(200, "Content Check Result", content_result_model)
    @ns_content_check.expect(parser)
    def post(self):
        """
        /content

        Returns detected flags and a censored version of the given content.

        Checks executed:
        - `contains_url`: If the content includes a URL
        - `blocked_word`: If the content includes a blocked word

        The censored version of the content will have all detected characters replaced with an asterisk `*`.
        """
        args = parser.parse_args(strict=True)
        content = args["content"]
        result = self.content_service.check_content(content)
        return result
    