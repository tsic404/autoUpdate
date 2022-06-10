
from os import makedirs, popen

def do_extra(app):
    makedirs("usr/bin/")
    popen("ln -sf ../../opt/apps/com.visualstudio.code/files/code/bin/code usr/bin/code").read()
