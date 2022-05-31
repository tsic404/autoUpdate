from infos.info import AbsSource
import yaml

class Source(AbsSource):
    def check(self):
        url ="http://cdn.apifox.cn/download/latest-linux.yml"
        yml = yaml.safe_load(self.get_text_by_url(url))
        return yml['files'][0]['url'] ,yml['version']