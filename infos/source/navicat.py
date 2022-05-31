

from infos.info import AbsSource
from bs4 import BeautifulSoup

class Source(AbsSource):
    def check(self):
        url = "http://navicat.com/en/products/navicat-premium-release-note"
        text = self.get_text_by_url(url)
        soup = BeautifulSoup(text)
        a = soup.find_all({"class": "note-title"})
        return a