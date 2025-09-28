from app.services.mail_validation.validator_manager import ValidatorManager
from flask_restx import Resource, Namespace, fields, Model, Api
from flask import request

ns_mail = Namespace('mail', description='Endpoint for Email Validation')
parser = ns_mail.parser()
parser.add_argument('mail', type=str, required=True, location='json')

@ns_mail.route('/')
class MailValidationResource(Resource):
    """
    A resource class for validating email addresses.
    """
    validator_manager = ValidatorManager()

    @ns_mail.expect(parser)
    def post(self):
        args = parser.parse_args(strict=True)
        email = args["mail"]
        return self.validator_manager.validate_mail(email)