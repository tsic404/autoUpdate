#!/bin/env python3

from infos.info import AbsSource

class Source(AbsSource):

    def check(self):
        url = "https://url.wiz.cn/u/linux_new"
        url = self.get_headers(url)['Location']
        d_url = r"https://get.wiz.cn/x/wiznote-desktop-(.*)-linux-x86_64.AppImage"
        url, ver = self.re_search(d_url, url)
        url = url.replace("?version=latest", "")
        return url, "1:"+ver
