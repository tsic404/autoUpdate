from os import makedirs, popen


def do_extra(app):
    appid= app.appid
    makedirs("usr/bin/")
    popen("ln -sf ../../opt/apps/" + appid + "/files/codium/bin/codium usr/bin/codium").read()