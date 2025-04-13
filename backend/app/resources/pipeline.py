import subprocess
from flask_restx import Resource, Namespace
from flask import request

from app.services.deep_check.pipeline_submitter import PipelineSubmitter


ns_pipeline = Namespace('pipeline', description='Endpoint to trigger a pipeline execution')

post_parser = ns_pipeline.parser()
post_parser.add_argument('content', type=str, required=True, location='json')


@ns_pipeline.route('/')
class FlaggedContentResource(Resource):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.submitter = PipelineSubmitter()

    def put(self):
        return self.submitter.run_pipeline()

    def get(self):
        return self.submitter.get_status()

    def post(self):
        post_parser.parse_args(request, strict=True)
        content = request.json["content"]
        return self.submitter.check_content_instant(content)
