#!/bin/env python3

from infos.info import AbsSource


class Source(AbsSource):
    def check(self):
        res = self.get_text_by_url("http://www.hostbuf.com/t/989.html")
        _, ver =  self.re_search(r"(\d{4}\.\d{1,2}\.\d{1,2}) 版本号(\d{1,2}\.\d{1,2}\.\d{1,2})", res)
        url = "http://dl.hostbuf.com/finalshell2/finalshell_linux.zip"
        return url,ver

