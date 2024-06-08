import imaplib
from typing import Literal, Tuple, Optional


class ImapConnection:
    def __init__(self, imap_mode: Literal['defoult', 'ssl'] = 'ssl'):
        self.imap_mode = imap_mode

    def make_connection(self,
                        mail_adress: str,
                        mail_password: str,
                        mail_args: Tuple[str, str]) -> Optional[imaplib.IMAP4]:
        if self.imap_mode == 'ssl':
            imap = imaplib.IMAP4_SSL(*mail_args)
            sts, res = imap.login(mail_adress, mail_password)
            if sts == "OK":
                return imap
            else:
                return None



