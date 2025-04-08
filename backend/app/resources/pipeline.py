import subprocess
from flask_restx import Resource, Namespace
from flask import request

from app.services.deep_check.pipeline_submitter import PipelineSubmitter


ns_pipeline = Namespace('pipeline', description='Endpoint to trigger a pipeline execution')

post_parser = ns_pipeline.parser()
post_parser.add_argument('content', type=str, required=True, location='json')


@ns_pipeline.route('/')
class FlaggedContentResource(Resource):
    
    def put(self):
        return PipelineSubmitter().run_pipeline()

    def get(self):
        return PipelineSubmitter().get_status()

    def post(self):
        post_parser.parse_args(request, strict=True)
        content = request.json["content"]
        return PipelineSubmitter().check_content_instant(content)
