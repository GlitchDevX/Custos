from flask_restx import Resource, Namespace
from flask import request

from app.services.set_config.config_setter import ConfigSetter

ns_config = Namespace('set-config', description='Endpoint to set config files')
parser = ns_config.parser()
parser.add_argument('file', type=str, required=True, location='json')
parser.add_argument('content', type=any, required=True, location='json')

@ns_config.route('/')
class ConfigResource(Resource):
    setter = ConfigSetter()

    @ns_config.expect(parser)
    def post(self):
        parser.parse_args(strict=True)
        
        filename = request.json["file"]
        content = request.json["content"]

        return self.setter.set_file(filename, content)