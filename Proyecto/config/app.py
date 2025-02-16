from config.database import *
from config.mail import *

class App:
    def __init__(self, path):
        smtp_server, port, user, password = [
            'sandbox.smtp.mailtrap.io',
            2525,
            '9a3c8223168f67',
            '367b96da5a548b'
        ]

        self.bd = Database(path)
        self.mail = Mail(smtp_server, port, user, password)
