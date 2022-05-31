from infos.info import AbsSource

class Source(AbsSource):
    def check(self):
        url = "https://url.zhumu.me/2c9c"
        url = self.get_headers(url)['Location']
        ver =  self.re_search(r'zhumu_(.*?)_amd64.deb', url)[1]
        return url, ver