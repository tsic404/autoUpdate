
from infos.info import AbsSource
from re import search
class Source(AbsSource):
    def check(self):
        url = "https://www.graebert.com/cad-software/download/ares-commander/linux/deb/latest"
        url = self.get_headers(url)['Location']

        ver = search(r'ARES-Commander-(.*?)-(.*?)-(.*?).deb', url)[2]
        return url, ver