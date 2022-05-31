

from infos.info import AbsSource


class Source(AbsSource):
    def check(self):
        url = "https://www.veracrypt.fr/en/Downloads.html"
        text = self.get_text_by_url(url)
        deb, ver = self.re_search(r"veracrypt-(.*)-Debian-10-amd64.deb", text)
        return self.re_search(r"https://(.*)"+deb, text)[0].replace("&#43;", "+"), ver
