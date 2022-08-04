
from cgitb import text
from re import search
from requests import get
from infos.info import AbsSource

class Source(AbsSource):
    def check(self):
        d_url = "https://download.owncloud.com/desktop/ownCloud/stable/(.*?)/linux-appimage/ownCloud-(.*?).AppImage"
        url ="https://owncloud.com/desktop-app/"
        res = self.get_text_by_url(url=url)
        res = search(d_url, res)
        return res.group(), res.groups()[1]