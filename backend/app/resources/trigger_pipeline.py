import subprocess
from flask_restx import Resource, Namespace
from flask import request


ns_trigger_pipeline = Namespace('trigger-pipeline', description='Endpoint to trigger a pipeline execution')

@ns_trigger_pipeline.route('/')
class FlaggedContentResource(Resource):

    def get(self):
        #TODO: trigger pipeline maybe with subprocess
        # subprocess.run()
        return { "code": "TRIGGERED" }
