#!/bin/env python3

from infos.info import AbsSource


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

from infos.info import AbsSource
import requests
from bs4 import BeautifulSoup
from re import search


class Source(AbsSource):
    
    def check(self):
        soup = BeautifulSoup(requests.get("https://filezilla-project.org/download.php?platform=linux64", headers=headers).text, features="html.parser")
        
        d_url = r'https://dl(.*?).cdn.filezilla-project.org/client/FileZilla_(.*?)_x86_64-linux-gnu.tar.bz2(.*)'
        for i in soup.find("div", {"class": "downloadbutton"}):
            try:
                res = search(d_url, i.attrs["href"])
                return res.group(), res.groups()[1]
            except AttributeError:
                pass
