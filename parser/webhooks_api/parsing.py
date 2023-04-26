import os
from dotenv import load_dotenv
import requests
from html.parser import HTMLParser

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

    def get_data_post(self):
        url = f'http://glazarev.atlassian.net/wiki/api/v2/blogposts/{self.id}?body-format=storage'
        response = requests.request(
            "GET",
            url,
            headers=self.HEADERS,
            auth=self.AUTH,
        )
        data = response.json().get('body').get('storage').get('value')
        return data

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
    print('Все элементы поста')
    print('------------------------------------')
    parser = Parser(man_id)
    body = parser.parse_body()
    print(body)
    print('Ссылка на ftp сервер которая содержится в посте')
    print('------------------------------------')
    link = parser.parse_ftp_link()
    print(link)


if __name__ == "__main__":
    main()