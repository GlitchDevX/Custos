from flask_restx import Resource, Namespace, fields

from app.services.configure.config_setter import ConfigSetter
from app.config_reader import ConfigReader
from app.utils.common_responses import ENDPOINT_DISABLED_MODEL

ns_config = Namespace('Config', description="""
Endpoints to modify and retrieve configuration.

All settings are split into namespaces reflecting the individual endpoints.

Available namespaces:
- `content_check`
- `deep_analysis`
- `mail_validation`
- `metrics`
""", path="/config")

put_parser = ns_config.parser()
put_parser.add_argument('namespace', type=str, required=True, location='json')
put_parser.add_argument('content', type=dict, required=True, location='json')

get_parser = ns_config.parser()
get_parser.add_argument('namespace', type=str, required=True)

put_success_model = ns_config.model("config_update_successful", {
    'CODE': fields.String("OK")
})
get_success_model = ns_config.model("config_retrieve_successful", {
    'property_name*': fields.String("Any")
})
not_found_model = ns_config.model("namespace_not_found", {
    'error': fields.String("NAMESPACE_NOT_FOUND"),
    'text': fields.String("Config Namespace not found")
})
endpoint_disabled_model = ns_config.model("endpoint_disabled", ENDPOINT_DISABLED_MODEL)

@ns_config.route('/', strict_slashes=False)
class ConfigResource(Resource):
    """
    A resource class for managing configuration files.
    This class provides endpoints to set and retrieve configuration settings.
    """
    setter = ConfigSetter()

    @ns_config.response(503, "Endpoint Disabled", endpoint_disabled_model)
    @ns_config.response(404, "Namespace not Found", not_found_model)
    @ns_config.response(200, "Update Success", put_success_model)
    @ns_config.expect(put_parser)
    def put(self):
        """
        /config

        Update the configuration for the specified namespace.
        """
        args = put_parser.parse_args(strict=True)
        
        filename = args["namespace"]
        content = args["content"]

        return self.setter.set_file(filename, content)

    @ns_config.response(503, "Endpoint Disabled", endpoint_disabled_model)
    @ns_config.response(404, "Namespace not Found", not_found_model)
    @ns_config.response(200, "Config Content", get_success_model)
    @ns_config.expect(get_parser)
    def get(self):
        """
        /config

        Retrieve the configuration for the specified namespace.
        """
        args = get_parser.parse_args(strict=True)
        namespace = args["namespace"]
        config = ConfigReader(namespace).get_all()

        if config is None:
            return {"error": "NAMESPACE_NOT_FOUND", "text": "Config Namespace not found" }, 404
        else:
            return config, 200