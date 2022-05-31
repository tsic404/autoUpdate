

from os import listdir, makedirs, popen


def do_extra(app):
    appid = app.appid
    makedirs("usr/lib/x86_64-linux-gnu/veyon/")
    shell = "ln -sf ../../../../opt/apps/" + appid + "/files/lib/x86_64-linux-gnu/veyon/{file} usr/lib/x86_64-linux-gnu/veyon/{file}"
    for i in listdir("opt/apps/" + appid + '/files/lib/x86_64-linux-gnu/veyon/'):
        popen(shell.format(file=i)).read()
