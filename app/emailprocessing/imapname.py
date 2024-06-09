from typing import Optional
# from re_functions import mail_validator


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


class IMAPServerArgs:
    def __init__(self, pochta: str = 'firstmail'):
        if pochta not in pochta_set:
            raise TypeError(f'Invalid mail. Name {pochta} not in {pochta_set}')
        self.pochta = pochta
        self.mail_adress = None

    def make_search(self, adress: str):
        # adress = myutils.mail_validator(adress)
        pass

    def get_imap_server_args(self, mail_adress: Optional[str] = None):
        if self.pochta is None:
            if mail_adress is not None:
                return self.make_search(mail_adress)
        else:
            return (emails_servers.get(self.pochta).get("server"),
                    emails_servers.get(self.pochta).get("port"))
