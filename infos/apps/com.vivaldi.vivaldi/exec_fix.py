

from os import popen


def do_extra(app):
    appid = app.appid
    desktop = 'opt/apps/' + appid + '/entries/applications/vivaldi-stable.desktop'
    shell = "sed -i 's|Exec=/usr/bin/vivaldi-stable|Exec=/opt/apps/com.vivaldi.vivaldi/files/vivaldi|g' " + desktop
    popen(shell).read()
