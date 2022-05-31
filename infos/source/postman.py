#!/bin/env python3

from infos.info import AbsSource


class Source(AbsSource):

    def check(self):
        url = "https://web.postman.com/tools/version/?platform=linux64&channel=stable"
        url = "https://www.postman.com/cache-1631836126608/pm/version.json"
        url = "https://dl.pstmn.io/api/version/latest?platform=linux64&channel=stable"
        res_json = self.get_json_by_url(url)
        url = "https://dl.pstmn.io/download/latest/linux64"
        return url, res_json['version']

