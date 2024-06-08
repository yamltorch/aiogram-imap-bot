import re
from typing import Tuple, Optional


def mail_validator(mail: str) -> Optional[str]:
    pat = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    if re.match(pat, mail):
        return mail
    else:
        return None
        # raise ValueError(f'{mail} is not a valid mail address')


def extract_email_and_password(input_string) -> Tuple[Optional[str], Optional[str]]:
    pattern = r'([^:]+):(.+)'

    matches = re.findall(pattern, input_string)

    if matches:
        return matches[0]
    else:
        return None, None