

from os import listdir, popen


def do_extra(app):
    appid = app.appid
    shell = "sed -i 's|/opt/emby-server|/opt/apps/" + appid + "/files|g' "
    dirs = "opt/apps/" + appid + "/files/usr/lib/systemd/system/"
    for i in listdir(dirs):
        popen(shell + dirs + i).read()
