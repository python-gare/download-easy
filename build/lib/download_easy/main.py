import requests
from pathlib import Path
from tqdm import tqdm
import click
import os
import time
import socket

class DownloadEasy(object):
    def __init__(self, url):
        self.url = url
        self.file_name = self.url.split("/")[-1]
        self.resume_header = {'Range':f'bytes=0-'}
        self.r = requests.get(self.url, stream=True, headers=self.resume_header, timeout=5)
        self.total_size = int(self.r.headers.get('content-length'))
        self.initial_pos = 0

    def file_check(self, out=os.getcwd()):
        try:
            self.resume_header = {'Range':f'bytes= {Path(os.path.join(out, self.file_name)).stat().st_size}-'}
            self.total_size = int(self.r.headers.get('content-length')) - Path(os.path.join(out, self.file_name)).stat().st_size
            self.r = requests.get(self.url, stream=True, headers=self.resume_header, timeout=5)
            return True
        except:
            return False

    def url_validate_check(self):
        pass

    def download_file(self, out=os.getcwd()):
        with open (os.path.join(out, self.file_name),'ab') as f:
            with tqdm(total=self.total_size, unit='B', unit_scale=True,desc=self.file_name,
                initial=self.initial_pos, ascii=True) as pbar:
                for chunk in self.r.iter_content(1024):
                    f.write(chunk)
                    pbar.update(len(chunk))




def checkInternetSocket(host="8.8.8.8", port=53, timeout=3):
    try:
        socket.setdefaulttimeout(timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
        return True
    except socket.error as ex:
        return False


@click.command()
@click.option('--out', type=click.Path(exists=True), default=os.getcwd(), help='Output Path Default is Current Path')
@click.option('--file_name', help='Default will be automatically fetch from url')
@click.argument('url')
def cli(url, out, file_name):
    """Download Big Files without worry!

    How to use

    download-easy https://www.sample-videos.com/video123/mp4/720/big_buck_bunny_720p_30mb.mp4

    """
    def download_main():
        try:
            if not checkInternetSocket():
                raise requests.ConnectionError

            obj1 = DownloadEasy(url)
            if file_name:
                obj1.file_name = file_name

            if obj1.file_check(out=out):
                click.echo("The file already is there, Will continue to download remaining files")
                obj1.download_file(out=out)
            else:
                click.echo("No File is there starting to download")
                obj1.download_file(out=out)

        except (requests.ConnectionError, requests.Timeout) as exception:
            time.sleep(2)
            click.echo("No internet connection.! Don't Worry When Connection come It will remain to continue")
            download_main()

    download_main()

if __name__ == "__main__":
    cli()
