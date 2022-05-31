
from infos.info import AbsSource

class Source(AbsSource):
    def check(self):
        v_url = "http://code.calibre-ebook.com/latest"
        version = self.get_text_by_url(v_url)
        dl_url = 'https://download.calibre-ebook.com/' + version + '/calibre-' + version + '-x86_64.txz'
        return dl_url, version
        