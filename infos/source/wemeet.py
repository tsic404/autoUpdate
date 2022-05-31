from infos.info import AbsSource

class Source(AbsSource):
    def check(self):
        url = "https://meeting.tencent.com/web-service/query-download-info?q=[{%22package-type%22:%22app%22,%22channel%22:%220300000000%22,%22platform%22:%22linux%22,%22arch%22:%22x86_64%22}]&nonce=fd8Ynsd07c6tjyczTa"
        d_json = self.get_json_by_url(url=url)
        ver = d_json['info-list'][0]['version']
        url = d_json['info-list'][0]['url']
        return url,ver
