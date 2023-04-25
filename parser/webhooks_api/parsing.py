import os
from dotenv import load_dotenv
import requests
from ftplib import FTP
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
    links = []
    def handle_data(self, data):
        self.links.append(data)
        return self.links


def get_files(link):
    domain = 'server-dev.astralinux.ru'
    ftp_dir = link.split(f'ftp://{domain}')[1][1:]
    print(ftp_dir)
    ftp = FTP(domain)
    ftp.login()
    ftp.cwd(ftp_dir) 
    ftp.retrlines('LIST')


def parse_last_post(id):
    url = f'http://glazarev.atlassian.net/wiki/api/v2/blogposts/{id}?body-format=storage'
    response = requests.request(
        "GET",
        url,
        headers=headers,
        auth=auth,
    )
    data = response.json().get('body').get('storage').get('value') # .get('title')
    parser = BodyParser()
    parser.feed(data)
    print(parser.links[3])
    return get_files(parser.links[3])


def main():
    # print(get_files())
    print(parse_last_post(786563))


if __name__ == "__main__":
    main()