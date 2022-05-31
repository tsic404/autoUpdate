#!/bin/env python3

from infos.info import AbsSource


class Source(AbsSource):
    def check(self):
        url = 'https://www.apipost.cn/dl.php?client=Linux&arch=x64'
        url= self.get_headers(url)['Location']
        _,ver = self.re_search(r'ApiPost_(.*)_amd64.deb', url)
        return url, ver
