
from genericpath import exists
from os.path import join
from os import listdir
from os.path import abspath
from yaml import YAMLObject, safe_load, dump
from git.repo import Repo
from scripts.utils import test_proxy_not_env, singleton
from scripts.sqlite import VerDB

@singleton
class configure(YAMLObject):
    def __init__(self, **entries) -> None:
        self.__dict__.update(entries)

    def __repr__(self) -> str:
        return dump(self)
    
    def test_net(self):
        test_proxy_not_env(self.net['proxy_ip'], self.net['proxy_port'])
    
    @property
    def default_permissions(self):
        permissions = self.app_default.get("default_permissioins")
        assert permissions is not None
        return permissions
    
    @property
    def default_debian(self):
        debian_info = self.app_default.get("default_debian")
        assert debian_info is not None
        return debian_info
    
    @property
    def upstream(self):
        upstream = join(self.info, "source")
        assert exists(upstream) is True
        return upstream

    def update_infos(self):
        return [abspath(join(self.info, "apps", c, c + ".yaml")) for c in listdir(join(self.info, "apps"))]
    
    def get_db(self):
        return VerDB(self)

def get_conf(file):
    f = open(file, "r+")
    conf = safe_load(f)
    conf = configure(**conf)
    f.close()
    return conf

def test():
    conf = get_conf("config.yaml")
    print(conf.update_infos())
    print(conf.test_net())

if __name__=="__main__":
    test()
