from bs4 import BeautifulSoup

from infos.info import AbsSource

from scripts.utils import get_ver_from_tag

class Source(AbsSource):
    def check(self):
        url = "https://www.freedownloadmanager.org/download-fdm-for-linux.htm"
        text = self.get_text_by_url(url)
        soup = BeautifulSoup(text, "html.parser")
        text = soup.find_all("span", {"class": "version"})[0].text.strip()
        ver = get_ver_from_tag(text).strip("64").strip(" for Linux")
        text = soup.find_all("a", {"class": "download_btn_new"})[0]['href']
        return (text, ver)