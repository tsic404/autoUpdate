#!/bin/env python3

from infos.info import AbsSource


class Source(AbsSource):
    def check(self):
        d_url = r"https://redirector.gvt1.com/edgedl/android/studio/ide-zips/(.*)/android-studio-(.*)-linux.tar.gz"
        res = self.get_text_by_url("https://developer.android.google.cn/studio")
        return self.re_search(d_url, res)
