from typing import Tuple, Optional, Union

from app.emailprocessing.imapconnection import ImapConnection
from app.emailprocessing.imapname import IMAPServerArgs
from app.emailprocessing.message import EmailMessage
from app.emailprocessing.re_functions import extract_email_and_password


class EmailCodeManager:
    def __init__(self,
                 mail_name: str = 'firstmail'):
        self.mail_name = mail_name
        self.mail_adress = None
        self.mail_password = None
        self.imap_server = None
        self.imap_args = None
        self.code = None

    def get_email_code(self,
                       mailpass: str) -> Union[Tuple[Optional[str], Exception], Tuple[Optional[str], int]]:

        try:
            self.mail_adress, self.mail_password = extract_email_and_password(mailpass)
        except Exception as e:
            print(f'Error in extract_email_and_password: {e}')
            return self.mail_adress, e

        try:
            self.imap_args = IMAPServerArgs(self.mail_name).get_imap_server_args()
        except Exception as e:
            print(f'Error in IMAPServerArgs: {e}')
            return self.mail_adress, e

        try:
            self.imap_server = ImapConnection(self.mail_adress, self.mail_password, self.imap_args).imap
        except Exception as e:
            print(f'Error in ImapConnection: {e}')
            return self.mail_adress, e

        try:
            self.code = EmailMessage(self.imap_server).get_code()
        except Exception as e:
            print(f'Error in EmailMessage: {e}')
            return self.mail_adress, e

        try:
            return self.mail_adress, int(self.code)
        except Exception as e:
            print(f'Error in int(code): {e}')
            return self.mail_adress, e
