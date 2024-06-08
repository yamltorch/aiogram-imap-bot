from enum import Enum
from typing import Optional
import re


def mail_validator(mail: str):
    pat = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    if re.match(pat, mail):
        return mail
    else:
        raise ValueError(f'{mail} is not a valid mail address')


pochta_set = {"rambler", "onet", "firstmail"}


emails_servers = {
    'rambler': {
        'server': 'imap.rambler.ru',
        'port': 993,
    },
    'onet': {
        'server': 'imap.poczta.onet.pl',
        'port': 993,
    },
    'firstmail': {
        'server': 'imap.firstmail.ltd',
        'port': 993,
    }
}


class IMAPname:
    def __init__(self, pochta: str):
        if pochta not in pochta_set:
            raise TypeError(f'Invalid mail. Name {pochta} not in {pochta_set}')
        self.pochta = pochta
        self.mail_adress = None

    def make_search(self, adress: str):
        # adress = mail_validator(adress)
        pass

    def get_imap_server(self, mail_adress: Optional[str]):
        if self.pochta is None:
            return self.make_search(mail_adress)
        else:
            return (emails_servers.get(self.pochta).get("server"),
                    emails_servers.get(self.pochta).get("port"))





