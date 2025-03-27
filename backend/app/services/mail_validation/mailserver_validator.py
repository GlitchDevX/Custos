from .validator_module import ValidatorModule


class MailserverValidator(ValidatorModule):

    def execute_check(self, email):
        pass
        # impl mailserver check via dns record domain