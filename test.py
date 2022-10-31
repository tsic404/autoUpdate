

from infos.source.owncloud import Source

from scripts.conf import get_conf

print(Source({"meta_info": {"appid": "test"} },get_conf("config.yaml"),True).check())