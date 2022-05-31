#!/bin/env python3


from infos.info import AbsSource


class Source(AbsSource):

    def check(self):
        d_url = r"https://download.mozilla.org/\?product=thunderbird-(.*)-SSL&os=linux64&lang=zh-CN"
        content = self.get_text_by_url("https://www.thunderbird.net/zh-CN/")
        _, ver = self.re_search(d_url, content)
        url = "https://download-installer.cdn.mozilla.net/pub/thunderbird/releases/{ver}/"\
              "linux-x86_64/en-US/thunderbird-{ver}.tar.bz2".replace("{ver}", ver)
        return url, ver
