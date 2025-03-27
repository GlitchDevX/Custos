from flask_restx import Resource, Namespace, fields, Model, Api
from flask import request

ns_mail = Namespace('validate-mail', description='Endpoint for Email Validation')
parser = ns_mail.parser()
parser.add_argument('mail', type=str, required=True, location='json')

@ns_mail.route('/')
class MailValidationResource(Resource):

    @ns_mail.expect(parser)
    def post(self):
        parser.parse_args(strict=True)
        return request.json, 200