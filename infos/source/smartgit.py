
from infos.info import AbsSource

class Source(AbsSource):
    def check(self):
        url = "https://www.syntevo.com/smartgit/download"
        d_url = "smartgit-linux-(.*).tar.gz"
        text = self.get_text_by_url(url)
        file,ver =  self.re_search(d_url, text)
        return "https://www.syntevo.com/downloads/smartgit/" + file, ver.replace('_', '.')
