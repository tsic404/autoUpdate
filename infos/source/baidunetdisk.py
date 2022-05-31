
from infos.info import AbsSource

class Source(AbsSource):
    def check(self):
        json = self.get_json_by_url("https://pan.baidu.com/disk/cmsdata?do=client&channel=chunlei&clienttype=0")['linux']
        d_url = json['url_1']
        ver = self.re_search(r'baidunetdisk_(.*)_amd64.deb', d_url)[1]
        return d_url,ver