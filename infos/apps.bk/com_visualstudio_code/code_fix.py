
from os import makedirs, popen


def do_extra(info):
    appid=info['meta']['appid']
    makedirs("usr/bin/")
    popen("ln -sf ../../opt/apps/com.visualstudio.code/files/code/bin/code usr/bin/code").read()
