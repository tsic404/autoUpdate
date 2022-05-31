
from infos.info import AbsSource

class Source(AbsSource):
    def check(self):
        d_url = r'https://download.nomachine.com/download/(.*)/Linux/nomachine_(.*)_amd64.deb'
        content = self.get_text_by_url("https://www.nomachine.com/download/download&id=3")
        print(self.re_search(d_url, content))