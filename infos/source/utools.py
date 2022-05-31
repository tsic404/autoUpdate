
from infos.info import AbsSource


class Source(AbsSource):
    def check(self):
        url = "https://u.tools/"
        res = self.get_text_by_url(url)
        publish_url = "https://publish.u-tools.cn/version2/"
        deb, ver = self.re_search(r'utools_(.*)_amd64.deb',res)
        return publish_url + deb, ver
