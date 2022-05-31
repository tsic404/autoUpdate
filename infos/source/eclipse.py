#!/bin/env python3

from infos.info import AbsSource

class Source(AbsSource):

    def check(self):
        code = self.meta_info['upstream']['info']['code']
        mirror = "https://mirrors.tuna.tsinghua.edu.cn/eclipse"
        json_data = self.get_json_by_url("https://api.eclipse.org/download/release/eclipse_packages")
        date = json_data['release_name']
        release_status = json_data['release_version']
        if len(json_data['packages'])== 0:
            return  (None , None)
        url = json_data['packages'][code + '-package']['files']['linux']['64']['url'][len("http://www.eclipse.org/downloads/download.php?file="):]
        return(mirror + url, date + "-" + release_status.upper())

