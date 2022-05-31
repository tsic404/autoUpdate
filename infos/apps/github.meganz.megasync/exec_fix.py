
from os import popen

def do_extra(app):
    appid = app.appid
    desktop = 'opt/apps/' + appid + '/entries/applications/megasync.desktop'
    shell = "sed -i 's|Exec=megasync|Exec=/opt/apps/" + appid + "/files/bin/megasync|g' " + desktop
    popen(shell).read()
