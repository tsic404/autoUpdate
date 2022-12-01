#!/bin/env python3
from os import popen

def do_extra(app):
    appid = app.appid
    desktop = 'opt/apps/' + appid + '/entries/applications/com.github.coslyk.MoonPlayer.desktop'
    shell = "sed -i 's|Exec=moonplayer|Exec=/opt/apps/com.github.moonplayer/files/AppRun|g' " + desktop
    popen(shell).read()
