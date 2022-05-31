from scripts.utils import Logger, ver_comp
from time import sleep
from requests import get
from re import search

class AbsSource:
    def __init__(self, app, config, need_update):
        self.__dict__.update(app)
        self.logger = Logger()
        self.config = config
        self.need_update = need_update
        self.max_try_count = config.failed_count
        self.appid = app['meta_info']['appid']
        self.force_update = app['meta_info'].get("force_update") if app['meta_info'].get("force_update") else False

    def check(self):
        raise NotImplementedError

    def run(self):
        try_count = 0
        ver = None
        url = None
        while (not ver) and try_count < self.max_try_count:
            try:
                url, ver = self.check()
            except BaseException as e:
                self.logger.error("can't get info for " + self.meta_info['appid'] + "  in " + str(try_count + 1) + " times.")
                self.logger.error("because of " + str(e))
                self.config.test_net()
                url=""
                sleep(30)
            finally:
                try_count += 1
        ver_db = self.config.get_db()
        need_update = ver_comp(ver_db.get_ver(self.appid), ver) 
        if self.force_update or (url and need_update):
            self.url = url
            self.version = ver
            self.need_update.append(self)

    def get_json_by_url(self, url, headers={}):
        return get(url, headers=headers).json()

    def get_text_by_url(self, url, headers={}):
        return get(url, headers=headers).text

    def re_search(self, re_rules, text):
        res = search(re_rules, text)
        return res.group(), res.groups()[0]

    def get_headers(self, url):
        return get(url, stream=True, allow_redirects=False).headers
