from os import makedirs, popen
from os.path import join
from shutil import copy

def do_extra(app):
    appid = app.appid
    makedirs("lib/systemd/system/")
    makedirs("opt/apps/" + appid + "/files/lib/systemd/system/")
    copy(join(app.originContentPath, "lib/systemd/system/veyon.service"),"opt/apps/" + appid + "/files/lib/systemd/system/veyon.service")
    popen("ln -sf ../../../../opt/apps/" + appid + "/files/lib/systemd/system/veyon.service lib/systemd/system/veyon.service").read()
    shell = "sed -i 's|ExecStart=/usr/bin/veyon-service|ExecStart=/opt/apps/" + appid +"/files/usr/bin/veyon-service|g' "
    popen(shell + "opt/apps/" + appid + "/files/lib/systemd/system/veyon.service").read()
