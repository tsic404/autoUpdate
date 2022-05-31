from infos.info import AbsSource


class Source(AbsSource):
    def check(self):
        repo = "https://repo.skype.com/deb/"
        release = "dists/stable/main/binary-amd64/Packages"
        res  =self.get_text_by_url(repo + release)
        ver = self.re_search(r'Version: (.*)',res)[1]
        filename = self.re_search(r'Filename: (.*)', res)[1]
        return repo + filename, ver
