#!/bin/env python3
from os import popen


def do_extra(app):
    appid = app.appid
    desktop = 'opt/apps/' + appid + '/entries/applications/bcompare.desktop'
    shell = "sed -i 's|Exec=bcompare|Exec=/opt/apps/" + appid + "/files/bin/bcompare|g' " + desktop
    popen(shell).read()
