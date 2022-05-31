
from infos.info import AbsSource

class Source(AbsSource):
    def check(self):
        url = "https://vivaldi.com/zh-hans/download/"
        text = self.get_text_by_url(url)
        return self.re_search(r"https://downloads.vivaldi.com/stable/vivaldi-stable_(.*?)_amd64.deb", text)
