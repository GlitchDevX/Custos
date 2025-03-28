def get_domain_from_email(email: str):
    return email[email.find('@')+1:]