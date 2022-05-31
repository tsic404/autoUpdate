

from os import popen


def do_extra(app):
    appid = app.appid
    desktop = 'opt/apps/' + appid + '/entries/applications/webtorrent-desktop.desktop'
    shell = "sed -i 's|Exec=webtorrent-desktop|Exec=/opt/apps/" + appid +"/files/bin/webtorrent-desktop|g' " + desktop
    popen(shell).read()
