from flask_restx import fields

ENDPOINT_DISABLED = {
    'error': "ENDPOINT_DISABLED",
    'text': "This endpoint is disabled. You can enable it in the config."
}, 503
ENDPOINT_DISABLED_MODEL = {
    'error': fields.String("ENDPOINT_DISABLED"),
    'text': fields.String("This endpoint is disabled. You can enable it in the config.")
}