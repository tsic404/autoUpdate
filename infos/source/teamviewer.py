from infos.info import AbsSource

class Source(AbsSource):
    def check(self):
        url = "https://download.teamviewer.com/download/linux/teamviewer_amd64.deb"
        url = self.get_headers(url)['Location']
        ver = self.re_search(r'teamviewer_(.*)_amd64.deb', url)[1]
        return url, ver