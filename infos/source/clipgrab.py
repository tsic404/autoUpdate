
from infos.info import AbsSource

class Source(AbsSource):
    def check(self):
        url = "https://clipgrab.org/"
        d_url = "https://download.clipgrab.org/ClipGrab-(.*)-x86_64.AppImage"
        res = self.get_text_by_url(url)
        return self.re_search(d_url, res)