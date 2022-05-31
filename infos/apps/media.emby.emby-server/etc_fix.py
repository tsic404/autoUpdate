
from genericpath import exists
from os.path import join
from shutil import move
from os import mkdir, popen, walk

def do_extra(app):
    appid = app.appid
    etc_prefix = "opt/apps/" + appid + "/files/etc/etc/"
    move(join(app.origin_extracted_path, "etc"),
            etc_prefix)
    etcs = walk(etc_prefix)
    mkdir("etc")
    for i,j,k in etcs:
        linkedPath = "etc/" + i[len(etc_prefix):]
        if not exists(linkedPath):
            mkdir(linkedPath)
        for file in k:
            popen("ln -sf " + "/" + i + "/" + file + " " + linkedPath + file)
