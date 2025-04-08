import subprocess
from flask_restx import Resource, Namespace
from flask import request

from app.services.deep_check.pipeline_submitter import PipelineSubmitter


ns_pipeline = Namespace('pipeline', description='Endpoint to trigger a pipeline execution')

pipeline_submitter = PipelineSubmitter()

@ns_pipeline.route('/')
class FlaggedContentResource(Resource):

    def post(self):
        return pipeline_submitter.run_pipeline()

    def get(self):
        return pipeline_submitter.get_status()
