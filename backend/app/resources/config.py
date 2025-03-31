from flask_restx import Resource, Namespace
from flask import request

from app.services.configure.config_setter import ConfigSetter
from app.config_reader import ConfigReader

ns_config = Namespace('config', description='Endpoint to set config files')
post_parser = ns_config.parser()
post_parser.add_argument('namespace', type=str, required=True, location='json')
post_parser.add_argument('content', type=any, required=True, location='json')

get_parser = ns_config.parser()
get_parser.add_argument('namespace', type=str, required=True)

@ns_config.route('/')
class ConfigResource(Resource):
    setter = ConfigSetter()

    @ns_config.expect(post_parser)
    def post(self):
        post_parser.parse_args(strict=True)
        
        filename = request.json["namespace"]
        content = request.json["content"]

        return self.setter.set_file(filename, content)
    
    @ns_config.expect(get_parser)
    def get(self):
        args = get_parser.parse_args(strict=True)
        namespace = args["namespace"]
        config = ConfigReader(namespace).get_all()

        if config is None:
            return {}, 404
        else:
            return config, 200