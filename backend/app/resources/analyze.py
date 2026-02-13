from flask_restx import Resource, Namespace, fields

from ..services.analyze.analyzer import AnalyzerService
from ..utils.common_responses import ENDPOINT_DISABLED_MODEL

ns_analyze = Namespace('Analyze', description='Endpoint for deep content analysis.', path="/analyze")

parser = ns_analyze.parser()
parser.add_argument('content', type=str, required=True, location='json')

analyze_result_model = ns_analyze.model("analyze_result", {
    'labels': fields.List(fields.String())
})
analyze_loading_model = ns_analyze.model("analyze_loading", {
    'code': fields.String("MODEL_TEMPORARY_UNAVAILABLE"),
    'text': fields.String("The detoxify model is still loading, please try again in a minute.")
})
analyze_unavailable_model = ns_analyze.model("analyze_unavailable", {
    'code': fields.String("MODEL_UNAVAILABLE"),
    'text': fields.String("The detoxify model is missing.")
})
endpoint_disabled_model = ns_analyze.model("endpoint_disabled", ENDPOINT_DISABLED_MODEL)


@ns_analyze.route('/', strict_slashes=False)
class AnalyzeResource(Resource):
    """
    A resource class for analysing content with the detoxify model.
    """
    analyzer_service = AnalyzerService()

    @ns_analyze.response(503, "Endpoint Disabled", endpoint_disabled_model)
    @ns_analyze.response(425, "Loading Model", analyze_loading_model)
    @ns_analyze.response(500, "Model Missing", analyze_unavailable_model)
    @ns_analyze.response(200, "Labels", analyze_result_model)
    @ns_analyze.expect(parser)
    def post(self):
        """
        /analyze

        Returns a list of labels detected by the detoxify multilingual model.

        Available labels are:
        `toxicity`, `severe_toxicity`, `obscene`, `threat`, `insult`, `identity_attack`, `sexual_explicit`
        """
        args = parser.parse_args(strict=True)
        content = args["content"]
        result = self.analyzer_service.analyze_content(content)
        return result
    