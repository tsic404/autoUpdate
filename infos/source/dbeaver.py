#!/bin/env python3

from infos.info import AbsSource


class Source(AbsSource):
    def check(self):
        url = "https://dbeaver.com/files/dbeaver-ee-latest-linux.gtk.x86_64.tar.gz"
        headres = self.get_headers(url)
        url = r"https://dbeaver.com/files/(.*)/dbeaver-ee-(.*)-linux.gtk.x86_64.tar.gz"
        return self.re_search(url, headres['location'])
