from flask_restx import Resource, Namespace
from flask import request

from app.services.configure.config_setter import ConfigSetter
from app.config_reader import ConfigReader

ns_config = Namespace('config', description='Endpoint to set config files')
put_parser = ns_config.parser()
put_parser.add_argument('namespace', type=str, required=True, location='json')
put_parser.add_argument('content', type=dict, required=True, location='json')

get_parser = ns_config.parser()
get_parser.add_argument('namespace', type=str, required=True)

@ns_config.route('/')
class ConfigResource(Resource):
    """
    A resource class for managing configuration files.
    This class provides endpoints to set and retrieve configuration settings.
    """
    setter = ConfigSetter()

    @ns_config.expect(put_parser)
    def put(self):
        args = put_parser.parse_args(strict=True)
        
        filename = args["namespace"]
        content = args["content"]

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