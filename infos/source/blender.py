
from infos.info import AbsSource

from re import search

from bs4 import BeautifulSoup

import requests

class Source(AbsSource):
    def check(self):
        d_url = "https://www.blender.org/download/release/Blender(.*)/blender-(.*)-linux-x64.tar.xz/"
        soup = BeautifulSoup(requests.get("https://www.blender.org/download/").text, features="html.parser")
        for i in soup.find_all(class_="js-download", dl_stats="Linux "):
            res = search(d_url, i.attrs["href"])
        url = self.get_headers(res.group(0))['refresh']
        return search("(?P<url>https?://[^\s]+)", url).group("url"), res.group(2)
        
