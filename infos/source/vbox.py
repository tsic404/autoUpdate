from urllib.parse import urlparse

from infos.info import AbsSource

class Source(AbsSource):
    def check(self):
        url = "https://www.virtualbox.org/wiki/Linux_Downloads"
        text = self.get_text_by_url(url)
        return self.re_search(r"https://download.virtualbox.org/virtualbox/(.*)/virtualbox-(.*)~Debian~buster_amd64.deb", text)
        
