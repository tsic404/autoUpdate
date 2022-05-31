from infos.info import AbsSource

class Source(AbsSource):
    def check(self):
        url = "https://telegram.org/dl/desktop/linux"
        url = self.get_headers(url)['Location']
        ver = self.re_search(r"tsetup.(.*).tar.xz", url)[1]
        return url,ver
        
