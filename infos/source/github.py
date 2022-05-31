#!/bin/env python3
from yaml import safe_load
from scripts.utils import get_ver_from_tag, ver_comp
from infos.info import AbsSource

headers = {}

with open("token.yaml") as f:
    token = safe_load(f)
    headers['Authorization'] = token['github']

class Source(AbsSource):

    def check(self):
        github = self.meta_info['upstream']['info']
        github_url = "https://api.github.com/repos/{author}/{project}/releases"
        github_url = github_url.replace("{author}", github['author']).replace("{project}", github['project'])
        json_data = self.get_json_by_url(github_url, headers)
        return self.get_latest(json_data, github['suffix'], github['prefix'])

    def get_latest(self,json, suffix, prefix):
        url = ""
        res = json[0]
        for i in json:
            if url.__eq__("") or ver_comp(get_ver_from_tag(res['tag_name']), get_ver_from_tag(i['tag_name'])):
                for asset in i['assets']:
                    if asset['name'].endswith(suffix) and asset['name'].startswith(prefix):
                        url = asset['browser_download_url']
                        res = i
        return url, get_ver_from_tag(res['tag_name'])
