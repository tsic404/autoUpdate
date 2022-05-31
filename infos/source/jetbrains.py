#!/bin/env python3

from infos.info import AbsSource


class Source(AbsSource):

    def check(self):
        code = self.meta_info['upstream']['info']['code']
        url = "https://data.services.jetbrains.com/products/releases?" \
              "code={code}&latest=true&type=release".replace("{code}", code)
        res_json = self.get_json_by_url(url)
        return res_json[code][0]['downloads']['linux']['link'], res_json[code][0]['version']
