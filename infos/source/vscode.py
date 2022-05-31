from urllib.parse import urlparse

from infos.info import AbsSource

class Source(AbsSource):
    def check(self):
        url = "https://code.visualstudio.com/sha/download?build=stable&os=linux-deb-x64"
        cdn = "https://vscode.cdn.azure.cn"
        _url = urlparse(self.get_headers(url)['Location'])
        url = cdn + _url.path
        ver = self.re_search(r"code_(.*)_amd64.deb", _url.path)[1]
        return url,ver
        
