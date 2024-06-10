import email
import imaplib
from typing import Literal
from .re_functions import get_vinted_code


class EmailMessage:

    EMAIL_PLACE = ["INBOX", "SPAM"]
    EMAIL_VIEW = ["UNSEEN", "ALL"]

    def __init__(self,
                 imap: imaplib.IMAP4,
                 view_mode: Literal["UNSEEN", "ALL"] = "UNSEEN"):
        self.imap = imap
        self.view_mode = view_mode

    @staticmethod
    def preprocessing(message) -> str:
        return str(email.message_from_bytes(message[0][1]))

    def get_message_indeces(self):
        for place in EmailMessage.EMAIL_PLACE:
            self.imap.select(place)
            _, val = self.imap.uid('search', self.view_mode)
            if val == [b'']:
                continue
            return val
        return None

    def get_message(self):
        indeces = self.get_message_indeces()
        if indeces is None:
            return None
        val = [x for x in indeces[0].split()][-1]
        res, msg = self.imap.uid('fetch', val, '(RFC822)')
        msg = EmailMessage.preprocessing(msg)
        return msg

    def get_code(self):
        message = self.get_message()
        if message is None:
            return None
        code = get_vinted_code(message)
        return code

    def close_connection(self):
        if self.imap is not None:
            try:
                self.imap.close()
            except Exception as e:
                print(f"Error closing mailbox: {e}")
            finally:
                self.imap.logout()
                self.imap = None

    def __del__(self):
        self.close_connection()


if __name__ == "__main__":
    print(EmailMessage.EMAIL_PLACE)
