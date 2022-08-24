from infos.info import AbsSource
from requests import post

class Source(AbsSource):
    def check(self):
        host = "https://www.scootersoftware.com"
        text = post(url = host + "/download.php", params={
            "zz": "dl4",
            "platform": "linux"
        }).text
        url, ver = self.re_search(r"bcompare-(.*?)_amd64.deb", text)
        return host + '/' + url, ver
