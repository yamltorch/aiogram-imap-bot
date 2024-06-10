import imaplib
from typing import Literal, Tuple, Optional


class ImapConnection:
    def __init__(self,
                 mail_adress: str,
                 mail_password: str,
                 mail_args: Tuple[str, str],
                 imap_mode: Literal['defoult', 'ssl'] = 'ssl'):
        self.imap_mode = imap_mode
        self.mail_adress = mail_adress
        self.mail_password = mail_password
        self.mail_args = mail_args
        self.imap: Optional[imaplib.IMAP4] = self.make_connection()

    def make_connection(self) -> Optional[imaplib.IMAP4]:
        if self.imap_mode == 'ssl':
            self.imap = imaplib.IMAP4_SSL(*self.mail_args)
            sts, res = self.imap.login(self.mail_adress, self.mail_password)
            if sts == "OK":
                return self.imap
            else:
                return None
