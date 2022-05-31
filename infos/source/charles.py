#!/bin/env python3

from email import header
from requests import post
from infos.info import AbsSource

from bs4 import BeautifulSoup


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

class Source(AbsSource):
    def check(self):
        url = "https://www.charlesproxy.com/latest-release/download.do"
        bs = BeautifulSoup(self.get_text_by_url(url), features="html.parser")
        ver = ""
        params = {}
        cookies = {}
        for element in bs.find_all("input"):
            params[element['name']] = element['value']
            if element['name'].__eq__("version"):
                ver = element['value']
            elif element['name'].__eq__("__csrf"):
                cookies['com.xk72.webparts.csrf'] = element['value']
        params['os'] = "linux64"
        bs = BeautifulSoup(post(url=url,headers=headers, cookies=cookies, params=params).text, features="html.parser")
        data = bs.find_all("meta", attrs={"http-equiv":"refresh"})[0]['content']
        url = self.re_search(r'url=(.*)', data)[1]
        return "https://www.charlesproxy.com" + url, ver