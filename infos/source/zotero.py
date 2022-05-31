
from infos.info import AbsSource

class Source(AbsSource):
    def check(self):
        durl = "https://www.zotero.org/download/client/dl?channel=release&platform=linux-x86_64"
        url = self.get_headers(durl)['location']
        _, ver = self.re_search(r"Zotero-(.*)_linux-x86_64.tar.bz2", url)
        return url, ver
