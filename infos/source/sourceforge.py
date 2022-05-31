#!/bin/env pythone3

from infos.info import AbsSource
import os
class Source(AbsSource):

    def check(self):
        sourceforge = self.meta_info['upstream']['info']
        project_name = sourceforge["project"]
        d_filename = sourceforge["d_filename"]
        url = "http://sourceforge.net/projects/{PROJECT_NAME}"
        url = url.replace("{PROJECT_NAME}" ,project_name)
        res = self.get_json_by_url(url + "/best_release.json")
        filename = res['platform_releases']['linux']['filename']

        dl_url = "https://sourceforge.net/projects/" + project_name + "/files" + filename + "/download"
        dl_url = self.get_headers(dl_url)['Location']

        _, ver = self.re_search(d_filename, os.path.basename(filename))

        return dl_url, ver
