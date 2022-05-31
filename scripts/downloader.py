import os
import requests
from time import sleep
from scripts.utils import Logger, singleton
from tqdm import tqdm
from urllib.parse import unquote
from urllib.request import urlopen, Request

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,"
              "application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,en;q=0.9",
    "Cache-Control": "max-age=0",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 "
                  "Safari/537.36",
}


@singleton
class Downloader:

    def __init__(self, config) -> None:
        self.config = config
        self.max_try_count = int(config.failed_count) if config.failed_count else 10
        self.logger = Logger()

    def download(self, url):
        dst = str(self.getfilename(url))
        req = Request(url, headers=headers)
        # get file size
        file_size = int(urlopen(req).info().get('Content-Length', -1))
        first_byte = 0
        # get downloaded size
        if os.path.exists(dst):
            first_byte = os.path.getsize(dst)
        else:
            first_byte = 0
        if first_byte >= file_size:
            return dst
        # set Downlaod headers
        header = {"Range": "bytes=%s-%s" % (first_byte, file_size)}
        # Download progess
        pbar = tqdm(
            total=file_size, initial=first_byte, file=self.logger.output,
            unit='B', unit_scale=True, desc=dst.split(os.sep)[-1])
        req = requests.get(url, headers=header, stream=True)
        with(open(dst, 'ab')) as f:
            for chunk in req.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
                    pbar.update(1024)
        pbar.close()
        return dst

    def getfilename(self, url):
        filename = ''
        headers = requests.head(url).headers
        if 'Content-Disposition' in headers and headers['Content-Disposition']:
            disposition_split = headers['Content-Disposition'].split(';')
            if len(disposition_split) > 1:
                if disposition_split[1].strip().lower().startswith('filename='):
                    file_name = disposition_split[1].split('=')
                    if len(file_name) > 1:
                        filename = unquote(file_name[1]).strip('"')
        if not filename and os.path.basename(url):
            if url.__contains__('?'):
                url = url.split('?')[0]
            filename = os.path.basename(url)
        return os.path.join(os.getcwd(), filename)

    def run(self, app):
            file = None
            try_count = 0
            while not file and try_count < self.max_try_count:
                try:
                    self.logger.warming("start downloading " + app.meta_info['appid'])
                    file = self.download(app.url)
                    self.logger.write('\n')
                except BaseException as e:
                    self.logger.error("failed to download " + app.url + " because of " + str(e))
                    self.config.test_net()
                    sleep(60)
                try_count += 1
            return file
