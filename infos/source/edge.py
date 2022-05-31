from infos.info import AbsSource
from re import search
class Source(AbsSource):
    def check(self):
        url = "https://go.microsoft.com/fwlink/?linkid=2149139"
        url = self.get_headers(url)['Location']
        ver = search(r'microsoft-edge-beta_(.*)_amd64.deb', url)[1]
        return url, ver