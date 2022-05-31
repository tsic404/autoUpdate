

from os import popen


def do_extra(app):
    appid = app.appid
    desktop = 'opt/apps/' + appid + '/entries/applications/realvnc-vncviewer.desktop'
    shell = "sed -i 's|Exec=vncviewer|Exec=/opt/apps/com.realvnc.viewer/files/bin/vncviewer|g' " + desktop
    popen(shell).read()
