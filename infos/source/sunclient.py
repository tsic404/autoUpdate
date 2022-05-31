from infos.info import AbsSource

class Source(AbsSource):
    def check(self):
        url = "https://sunlogin.oray.com/zh_CN/download/download?id=72&x64=1&os=Ubuntu/Deepin"
        url = self.get_headers(url)['Location']
        return self.re_search(r'https://down.oray.com/sunlogin/linux/sunloginclient-(.*?)-amd64.deb', url)