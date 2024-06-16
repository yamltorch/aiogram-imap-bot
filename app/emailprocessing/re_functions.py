import re
from typing import Tuple, Optional
from bs4 import BeautifulSoup


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


# def get_vinted_code(page: str):
#     soup = BeautifulSoup(page, 'lxml')
#
#     mail_code = soup.find("p").find_all("p")[1].text
#     return mail_code


def get_vinted_code(html_content):
    # Парсим HTML
    soup = BeautifulSoup(html_content, 'lxml')
    # Находим все блоки <p>
    paragraphs = soup.find_all('p')

    # Регулярное выражение для поиска числа из 4 или 6 цифр
    number_pattern = re.compile(r'\b(\d{4}|\d{6})\b')

    matching_paragraphs = []

    for p in paragraphs:
        text = p.get_text()
        # Найти все числа в тексте
        all_numbers = re.findall(r'\b\d+\b', text)
        # Проверить если есть ровно одно число и оно состоит из 4 или 6 цифр
        if len(all_numbers) == 1 and number_pattern.match(all_numbers[0]):
            matching_paragraphs.append(p.text)
    a = "\n".join(matching_paragraphs)
    return a
