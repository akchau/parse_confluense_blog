from ftplib import FTP

class Comnnection:
    DOMAIN = 'server-dev.astralinux.ru'

    def __init__(self, link):
        self.link = link

    def get_path(self):
        ftp_dir = self.link.strip().split(f'ftp://{self.DOMAIN}/')[1]
        return ftp_dir

    def get_connection(self):
        ftp = FTP(self.DOMAIN)
        ftp.login()
        return ftp

    def get_files(self):
        ftp = self.get_connection()
        path = self.get_path()
        print(path)
        ftp.cwd(path)
        ftp.retrlines('LIST')