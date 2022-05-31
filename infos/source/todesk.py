
from infos.info import AbsSource

class Source(AbsSource):
    def check(self):
        url = "https://www.todesk.com/linux.html"
        d_url = r"https://dl.todesk.com/linux/todesk_(.*?)_amd64.deb"
        text = self.get_text_by_url(url)
        print(text)
        url,ver =  self.re_search(d_url, text)
        return url[1:-4], ver
