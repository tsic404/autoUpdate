

from os import popen


def do_extra(app):
    appid = app.appid
    desktop = 'opt/apps/' + appid + '/entries/applications/freedownloadmanager.desktop'
    shell = "sed -i 's|Exec=/opt/freedownloadmanager/fdm|Exec=/opt/apps/org.freedownloadmanager.fdm/files/fdm|g' " + desktop
    popen(shell).read()
