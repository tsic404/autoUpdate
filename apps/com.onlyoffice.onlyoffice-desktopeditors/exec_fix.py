#!/usr/bin/env python3
from os import popen
def do_extra(app):
    appid = app.appid
    desktop = 'opt/apps/' + appid + '/entries/applications/onlyoffice-desktopeditors.desktop'
    shell = "sed -i 's|Exec=desktopeditors|Exec=/opt/apps/com.onlyoffice.onlyoffice-desktopeditors/files/bin/desktopeditors|g' " + desktop
    popen(shell).read()