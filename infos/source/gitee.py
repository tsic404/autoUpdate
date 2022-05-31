#!/bin/env python3
from infos.info import AbsSource


class Source(AbsSource):

    def check(self):
        author = self.info['meta']['gitee']['author']
        project = self.info['meta']['gitee']['project']
        url = "https://gitee.com/api/v5/repos/" \
            "{author}/{project}" \
            "/releases".replace("{author}", author).replace("{project}", project)
        res = self.get_json_by_url(url)
        return  

