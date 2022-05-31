from infos.info import AbsSource
from re import search

class Source(AbsSource):
    def check(self):
        url = "https://www.softmaker.com/en/softmaker-office-download"
        text = self.get_text_by_url(url)
        deb = "https://www.softmaker.net/down/softmaker-office-(.*)_amd64.deb"
        url, ver = self.re_search(deb, text)
        return url, ver