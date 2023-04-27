import os
import sys
from dotenv import load_dotenv
import requests
from html.parser import HTMLParser
from pathlib import Path

sys.path.append(os.path.join(Path(__file__).resolve().parent.parent.parent, ''))

from parser.parser.settings import BASE_DIR

load_dotenv()

username = os.getenv('USERNAME')
password = os.getenv('PASSWORD')

auth = requests.auth.HTTPBasicAuth(username, password)
headers = {
    "Accept": "application/json",
    "body-format": "atlas_doc_format"
}


class BodyParser(HTMLParser):
    elements = []
    def handle_data(self, data):
        self.elements.append(data)
        return self.elements


class Parser:
    USERNAME: str = os.getenv('USERNAME')
    PASSWORD: str = os.getenv('PASSWORD')
    AUTH = requests.auth.HTTPBasicAuth(USERNAME, PASSWORD)
    HEADERS: dict = {
        "Accept": "application/json",
        "body-format": "atlas_doc_format"
    }

    def __init__(self, id):
        self.id = id

    def check_env(self):
        return os.path.isfile(os.path.join(BASE_DIR.resolve().parent, '.env'))

    def get_data_post(self):
        url = f'http://glazarev.atlassian.net/wiki/api/v2/blogposts/{self.id}?body-format=storage'
        response = requests.request(
            "GET",
            url,
            headers=self.HEADERS,
            auth=self.AUTH,
        )
        data = response.json()
        data_of_post = data.get('body').get('storage').get('value')
        return data_of_post

    def parse_body(self):
        parser = BodyParser()
        parser.feed(self.get_data_post())
        return parser.elements
    
    def parse_ftp_link(self):
        ftp_link = self.parse_body()[3]
        return ftp_link


def main():
    print('Тестирование модуля парсинга постов:')
    man_id = input('Укажите id поста вручную: ')
    parser = Parser(man_id)
    print('Проверка наличия .env-файла с переменными')
    print('------------------------------------')
    if parser.check_env():
        print('Файл .env существует')
        print('Все элементы поста')
        print('------------------------------------')
        body = parser.parse_body()
        print(body)
        print('Ссылка на ftp сервер которая содержится в посте')
        print('------------------------------------')
        link = parser.parse_ftp_link()
        print(link)
    else:
        print('Файл .env НЕ существует')


if __name__ == "__main__":
    main()