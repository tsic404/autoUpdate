

from os import listdir, makedirs, popen
from os.path import join
from shutil import move


def do_extra(app):
    appid = app.appid
    move(join(app.origin_extracted_path, "etc"),
            "opt/apps/" + appid + "/files/etc")
    makedirs("etc/systemd/system/")
    services = listdir("opt/apps/" + appid + "/files/etc/systemd/system/")
    for i in services:
        popen("ln -sf ../../../opt/apps/" + appid + "/files/etc/systemd/system/" + i + " etc/systemd/system/" + i).read()
        popen("sed -i 's|/usr/|/opt/apps/" + appid +"/files/|g' opt/apps/" + appid + "/files/etc/systemd/system/" + i ).read()
    