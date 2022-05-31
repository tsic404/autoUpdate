
from infos.info import AbsSource

class Source(AbsSource):
    def check(self):
        url = "https://www.realvnc.com/en/connect/download/viewer/linux/"
        text = self.get_text_by_url(url)
        url, ver = self.re_search(r"/download/file/viewer.files/VNC-Viewer-(.*)-Linux-x64.deb", text)
        return "https://www.realvnc.com" + url, ver
