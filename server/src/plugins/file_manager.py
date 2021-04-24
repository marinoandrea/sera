import os
from ftplib import FTP_TLS
from uuid import uuid4

from .interfaces import FileManager


class FTPFileManager(FileManager):
    # NOTE(andrea): we currently use FTP
    # to store files in a development VPS.
    # Our production application should use AWS S3.
    ftp_user: str
    ftp_pass: str
    ftp_host: str
    static_folder: str

    def __init__(self):
        self.ftp_user = os.getenv('FTP_USER', '')
        self.ftp_pass = os.getenv('FTP_PASSWORD', '')
        self.ftp_host = os.getenv('FTP_HOST', '')
        self.static_folder = os.getenv('STATIC_FOLDER', 'static')

        if (
            self.ftp_user == '' or
            self.ftp_pass == '' or
            self.ftp_host == ''
        ):
            raise RuntimeError('Missing FTP configuration.')

    def store_file(self, temp_path: str) -> str:
        conn = FTP_TLS(host=self.ftp_host)
        conn.set_debuglevel(2)
        conn.login(
            user=self.ftp_user,
            passwd=self.ftp_pass,
        )
        conn.prot_p()

        ext = temp_path.split('.')[-1]
        file_name = f'{str(uuid4())}.{ext}'
        storage_path = f'{self.static_folder}/{file_name}'
        with open(temp_path, 'rb') as f:
            conn.storbinary(f'STOR {storage_path}', f)

        conn.quit()

        return f'https://{self.ftp_host}/sera/{file_name}'
