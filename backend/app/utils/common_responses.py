from flask_restx import fields

ENDPOINT_DISABLED = {
    'code': "ENDPOINT_DISABLED",
    'text': "This endpoint is disabled. You can enable it in the config."
}, 503
ENDPOINT_DISABLED_MODEL = {
    'code': fields.String("ENDPOINT_DISABLED"),
    'text': fields.String("This endpoint is disabled. You can enable it in the config.")
}