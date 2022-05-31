from infos.info import AbsSource

class Source(AbsSource):
    def check(self):
        url = "https://getsession.org/linux"
        headers = self.get_headers(url)
        url = headers['location']
        _, ver = self.re_search(r"session-desktop-linux-x86_64-(.*).AppImage", url)
        return url, ver