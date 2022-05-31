#!/bin/env python3

from infos.info import AbsSource


class Source(AbsSource):

    code = {
        "zh" : (
            "https://download-redirect.firefox.com.cn/?product=firefox-latest-ssl&os=linux64&lang=zh-CN",
            r"https://download-ssl.firefox.com.cn/releases/firefox/(.*)/zh-CN/Firefox-latest-x86_64.tar.bz2"),
        "nal": (
            "https://download.mozilla.org/?product=firefox-latest-ssl&os=linux64&lang=en-US",
            r"https://download-installer.cdn.mozilla.net/pub/firefox"
            "/releases/(.*)/linux-x86_64/en-US/firefox-(.*).tar.bz2"
        )
    }

    def check(self):
        url, d_url = self.code[self.meta_info['upstream']['info']['code']]
        reponse = self.get_headers(url)
        return self.re_search(d_url, reponse['Location'])

