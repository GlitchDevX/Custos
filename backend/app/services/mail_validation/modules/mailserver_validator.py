import smtplib
import socket
from typing import Set
import dns.resolver

from ..mail_utils import get_domain_from_email
from ..validation_result import ValidationResult
from .validator_module import ValidatorModule

class MailserverValidator(ValidatorModule):

    _successful_cache: Set[str] = set()

    _no_mailserver = ValidationResult(False, "NO_SERVER", "The Mailserver is not reachable")
    _ok_result = ValidationResult(True, "OK", "Everything okay")

    def __init__(self, config):
        self.config = config
    
    def _get_mail_servers(_, domain):
        try:
            mail_servers = dns.resolver.resolve(domain, 'MX', raise_on_no_answer=False)
            servers_dict = {}
            for server in mail_servers:
                priority, host = server.to_text().split(' ')
                servers_dict[host] = int(priority)

            sorted_servers_tuples = sorted(servers_dict.items(), key=lambda x: x[1])
            sorted_servers = list(map(lambda tuple: tuple[0], sorted_servers_tuples))

            return sorted_servers
        
        except dns.resolver.NXDOMAIN:
            pass
            # MAIL_INVALID_DOMAIN
        
        return []

    def _check_mail_servers(_, mail_host: str, email: str):
        print(f"Will check mail server with host: {mail_host}")
        
        try:
            server = smtplib.SMTP()
            server.set_debuglevel(0)

            server.connect(mail_host)
            server.helo("custus.com")
            server.mail("me@custos.com")
            code, message = server.rcpt(email)
            server.quit()
        
            print(f"Got Code {code} when testing mail host: {mail_host}. Response Message: '{message.decode()}'")
            return code == 250
        
        except smtplib.SMTPServerDisconnected as e:
            print(e)
            # MAIL_SMTP_DISCONNECT
        except smtplib.SMTPConnectError as e:
            print(e)
            # MAIL_SMTP_CONNECTION_ERROR
        except socket.timeout as e:
            print(e)
            # MAIL_SMTP_TIMEOUT

        return False


    def execute_check(self, email):
        domain = get_domain_from_email(email)
        
        servers = self._get_mail_servers(domain)
        if len(servers) == 0:
            return self._no_mailserver
        
        if not self.config.get("smtpHelo"):
            return self._ok_result
        
        if email in self._successful_cache:
            print(f"Email found in valid cache: {email}")
            return self._ok_result
        
        valid = False
        for server in servers:
            valid = self._check_mail_servers(server, email)
            if valid:
                self._successful_cache.add(email)
                break
        
        return self._ok_result if valid else self._no_mailserver
