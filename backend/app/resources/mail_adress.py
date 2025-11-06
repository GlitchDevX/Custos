from app.services.mail_validation.validator_manager import ValidatorManager
from flask_restx import Resource, Namespace, fields

from app.utils.common_responses import ENDPOINT_DISABLED_MODEL

ns_mail = Namespace('Mail', description='Endpoint for validating emails.', path="/mail")
parser = ns_mail.parser()
parser.add_argument('mail', type=str, required=True, location='json')

mail_result_model = ns_mail.model("mail_result", {
    'code': fields.String(),
    'text': fields.String()
})
endpoint_disabled_model = ns_mail.model("endpoint_disabled", ENDPOINT_DISABLED_MODEL)

@ns_mail.route('/', strict_slashes=False)
class MailValidationResource(Resource):
    """
    A resource class for validating email addresses.
    """
    validator_manager = ValidatorManager()

    @ns_mail.response(503, "Endpoint Disabled", endpoint_disabled_model)
    @ns_mail.response(200, "Mail Validation Result", mail_result_model)
    @ns_mail.expect(parser)
    def post(self):
        """
        /mail

        Returns a code and user-friendly text for the given email address.

        The code depends on the check the email failed at.

        Possible codes:
        - `OK`: All checks passed
        - `FORMAT_INVALID`: Invalid email format
        - `DISPOSABLE`: Domain of the email was marked disposable
        - `NO_SERVER`: The domain of the email does not have a mail server
        - `NO_ADDRESS`: The mail server does not have the given email address
        - `INVALID_DOMAIN`: Could not resolve dns records of domain
        - `SMTP_DISCONNECT`: The smtp server disconnected while checking email
        - `SMTP_CONNECTION_ERROR`: A smpt error occurred while checking email
        - `SMTP_TIMEOUT`: The smtp server timed out while checking email
        """
        args = parser.parse_args(strict=True)
        email = args["mail"]
        return self.validator_manager.validate_mail(email)