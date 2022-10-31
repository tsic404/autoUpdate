
from cgitb import text
from re import search
from requests import get
from infos.info import AbsSource

class Source(AbsSource):
    def check(self):
        d_url = "https://download.owncloud.com/desktop/ownCloud/stable/(.*?)/linux-appimage/"
        url ="https://owncloud.com/desktop-app/"
        res = self.get_text_by_url(url=url)
        res = search(d_url, res)
        return res.group() + "ownCloud-" + res.groups()[0] + ".AppImage", res.groups()[0]