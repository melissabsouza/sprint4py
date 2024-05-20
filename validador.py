import re

def validador_email(email_cadastro):
    regex = r'^[\w.-]+@[a-z\d]+\.[\w]{2,}$'
    return re.match(regex, email_cadastro) is not None