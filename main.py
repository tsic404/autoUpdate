#!/bin/env python3

from lib2to3.pytree import Base
import sys
from os.path import join, dirname
from tempfile import mktemp
from package import App
from infos.info import AbsSource
from scripts.conf import get_conf
from yaml import safe_load
from scripts.downloader import Downloader
from scripts.utils import Logger, import_module_from, run_in
from threading import Thread

class client:
    def __init__(self, conf) -> None:
        self.config = get_conf(conf)
        self.need_update = list()
        
    def add_runer(self) -> list:
        infos = self.config.update_infos()
        threads = list()
        for i in infos:
            with open(i) as f:
                app = safe_load(f)
                app.__setitem__("app_conf_path", dirname(i))
                app.__setitem__("origin_extracted_path", mktemp(prefix=self.config.unpack_path))
                app.__setitem__("package_path", mktemp(prefix=self.config.workspace))
                with import_module_from(join(self.config.info, "source"), app['meta_info']['upstream']['from']) as upstream:
                    source = upstream.Source(app, self.config, self.need_update)
                    if isinstance(source, AbsSource):
                        threads.append(Thread(target=source.run, name=app['meta_info']['appid']))
        return threads

    def package(self):
        for app in self.need_update:
            with run_in(self.config.download_path):
                app.origin_file = Downloader(self.config).run(app)
            app = App(config=self.config, app=app.__dict__)
            app.run()
                
                
    def add_single_one(self, appid):
        with open(join(self.config.info, "apps" ,appid, appid + ".yaml")) as f:
            app = safe_load(f)
            app.__setitem__("app_conf_path", join(self.config.info, "apps", appid))
            app.__setitem__("origin_extracted_path", mktemp(prefix=self.config.unpack_path))
            app.__setitem__("package_path", mktemp(prefix=self.config.workspace))
            app['meta_info'].__setitem__("force_update", True)
            with import_module_from(join(self.config.info, "source"), app['meta_info']['upstream']['from']) as upstream:
                source = upstream.Source(app, self.config, self.need_update)
                if isinstance(source, AbsSource):
                    source.run()

    def add_all(self):
        threads = self.add_runer()
        for thread in threads:
            thread.start()
            thread.join()
    
    def call_hooks(self, app):
        hooks = self.config.finished_hooks
        hooks_path = hooks['path']
        hooks = hooks['hooks']
        for hook in hooks:
            with import_module_from(path=hooks_path, module=hook) as hook:
                hook.call(app)
    
    def run(self, appid):
        if appid:
            self.add_single_one(appid=appid)
        else:
            self.add_all()
        self.package()

def main():
    argv = sys.argv
    appid=argv[1] if len(argv) >= 2 else None
    client("config.yaml").run(appid=appid)

if __name__=="__main__":
    sys.exit(main())
