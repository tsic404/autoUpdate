# -*- coding:utf-8 -*-  
from infos.info import AbsSource
from json import loads
class Source(AbsSource):

    def check(self):
        json = "https://y.qq.com/download/download.js"
        json = self.get_text_by_url(json)[18:-1]
        json = loads(json)
        url = json['data'][15]['Flink1']
        ver = json['data'][15]['Fversion'][4:]
        return (url, ver)