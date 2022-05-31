#!/bin/env python3

from infos.info import AbsSource


class Source(AbsSource):
    def check(self):
        url = "https://omahaproxy.appspot.com/linux"
        ver= self.get_text_by_url(url)
        print(ver)
        url ="https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb"
        return url, ver
