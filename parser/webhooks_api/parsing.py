import os
from dotenv import load_dotenv
import requests
from ftplib import FTP

load_dotenv()

username = os.getenv('USERNAME')
password = os.getenv('PASSWORD')

auth = requests.auth.HTTPBasicAuth(username, password)
headers = {
   "Accept": "application/json",
   "body-format": "atlas_doc_format"
}

def get_files(links):
    domain = 'server-dev.astralinux.ru'
    ftp = FTP(domain)
    ftp.login()
    ftp.cwd('maintainers/frozen/alse-X.7/1.7/RC/1.7.4.7') 
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
   return data


def main():
    print(get_files())


if __name__ == "__main__":
    main()