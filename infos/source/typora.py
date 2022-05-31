#!/bin/env python3

from infos.info import AbsSource
import requests
from bs4 import BeautifulSoup


class Source(AbsSource):
    
    def check(self):
        soup = BeautifulSoup(requests.get("https://typora.io/releases/stable.html").text, features="html.parser")
        
        d_url = r'https://download.typora.io/linux/typora_(.*)_amd64.deb'
        for i in soup.find_all(class_='download-btn linux'):
            try:
                url,ver = self.re_search(d_url, i.attrs["href"])
            except AttributeError:
                pass
        return url,ver
