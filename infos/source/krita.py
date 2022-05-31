#!/bin/env python3

from infos.info import AbsSource


class Source(AbsSource):

    def check(self):
        d_url = r"https://download.kde.org/stable/krita/(.*)/krita-(.*)-x86_64.appimage"
        res = self.get_text_by_url("https://krita.org/en/download/krita-desktop/")
        url, ver = self.re_search(d_url, res)
        ver = "1:" + ver
        return url, ver
