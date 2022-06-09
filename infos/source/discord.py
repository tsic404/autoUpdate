from infos.info import AbsSource
from re import search
class Source(AbsSource):
    def check(self):
        url = "https://discord.com/api/download?platform=linux&format=deb"
        url = self.get_headers(url)['location']
        ver = search(r'discord-(.*?).deb', url)[1]
        return url, "1:" + ver
