import os
from dotenv import load_dotenv
import requests

load_dotenv()

username = os.getenv('USERNAME')
password = os.getenv('PASSWORD')

auth = requests.auth.HTTPBasicAuth(username, password)
headers = {
   "Accept": "application/json",
   "body-format": "atlas_doc_format"
}

def parse_last_post(id):
   url = f'http://glazarev.atlassian.net/wiki/api/v2/blogposts/{id}?expand=body,version/'
   response = requests.request(
      "GET",
      url,
      headers=headers,
      auth=auth,
   )
   data = response.json() # .get('title')
   return data


def main():
    print(parse_last_post())


if __name__ == "__main__":
    main()