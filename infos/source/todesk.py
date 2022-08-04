
from infos.info import AbsSource

class Source(AbsSource):
    def check(self):
        url = "https://www.todesk.com/js/common.js"
        d_url = r"https://dl.todesk.com/linux/todesk_(.*?)_amd64.deb"
        text = self.get_text_by_url(url)
        url,ver =  self.re_search(d_url, text)
        return url, ver
